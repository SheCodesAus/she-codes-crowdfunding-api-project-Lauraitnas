from rest_framework import serializers
from .models import Category, Project, Pledge, Comments, Association
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField()


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        exclude = ['visible']
    


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    anonymous = serializers.BooleanField()
    supporter = serializers.SlugRelatedField(
        slug_field='username',
        queryset=get_user_model().objects.all()
    )
    project_id = serializers.IntegerField()
    # supporter_view = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class AssociationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    
    class Meta:
        model = Association
        fields = ('id', 'association_number', 'association_name', 'location', 'forest_image', 'user')

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()
    association = AssociationSerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field="slug", queryset=Category.objects.all())
    # owner = serializers.CharField(max_length=200)
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    association = AssociationSerializer(read_only=True)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.association = validated_data.get('association', instance.association)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance






