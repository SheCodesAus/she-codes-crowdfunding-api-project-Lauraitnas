from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serialiazer = ProjectSerializer(projects, many=True)
        return Response(serialiazer.data)