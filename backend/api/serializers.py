from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # model is the Model we want to serialize. In this case it is the User model from django.
        fields = ["id", "username", "password"] # All the fields needed to create a User and to return a User
        extra_kwargs = {"password": {"write_only": True}} # Tells django to accept passwords but not to return a password
    
    # This method is called whenever we create a new version of this User
    def create(self, validated_data): # Accepts the fields that have already been verified
        print(validated_data)
        user = User.objects.create_user(**validated_data) # Create User
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}