# from email.policy import default
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password





class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    image = serializers.URLField()
    bio = serializers.CharField(max_length=200)
    social = serializers.CharField(max_length=200,)


    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.social=validated_data.get('social', instance.social)
        instance.save()
        return instance





class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'bio', 'image', 'social')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            bio=validated_data['bio'],
            image=validated_data['image'],
            social=validated_data['social']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user