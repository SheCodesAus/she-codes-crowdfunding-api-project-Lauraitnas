from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Association, Project, Pledge, Comments, Category
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, CommentsSerializer, CategorySerializer, AssociationSerializer
from django.http import Http404
from rest_framework import status, permissions, generics, exceptions
from .permissions import IsOwnerOrReadOnly, IsAuthorOrReadOnly, IsProjectAssociationOrReadOnly
from django.core.exceptions import ObjectDoesNotExist


class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


#get category by slug
class CategoryDetail(APIView):
    
    def get_object(self, **kwargs):
        try:
            if "slug" in kwargs:
                return Category.objects.get(slug=kwargs["slug"])
            return Category.objects.get(pk=kwargs["pk"])
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, **kwargs):
        category = self.get_object(**kwargs)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

#get all categories

class CategoryList(generics.ListCreateAPIView):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


#get pledge by id
class PledgeDetail(APIView):
    
    def get_object(self, pk):
        try:
            p = Pledge.objects.get(pk=pk)
            if p.is_anonymous:
                p.supporter = None
            return p
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

        

#get all projects
class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.associations:
            raise exceptions.PermissionDenied("user has no associations")
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(association=request.user.associations)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsProjectAssociationOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CommentListApi(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.filter(visible=True)
    serializer_class = CommentsSerializer

class CommentDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Comments.objects.filter(visible=True)
    serializer_class = CommentsSerializer


class AssociationList(generics.ListCreateAPIView):

    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


    def perform_create(self, serializer):
        try:
            if self.request.user.associations:
                raise exceptions.ValidationError("you already have an association")
        except ObjectDoesNotExist:
            pass
        serializer.save(user=self.request.user)


class AssociationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, username):
        try:
            association = Association.objects.select_related("user").get(user__username=username)
            self.check_object_permissions(self.request, association)
            return association
        except Association.DoesNotExist:
            raise Http404

    def get(self, request, username):
        association = self.get_object(username)
        serializer = AssociationSerializer(association)
        return Response(serializer.data)
    
    def put(self, request, username):
        association = self.get_object(username)
        data = request.data
        serializer = AssociationSerializer(association, data=data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)