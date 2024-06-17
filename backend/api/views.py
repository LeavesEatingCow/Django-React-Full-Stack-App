from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

#   For all generic classes as long as you specify the serializer_class, permission_classes, and queryset it'll work


class NoteListCreate(generics.ListCreateAPIView):   #   ListCreate will list notes or create a new note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  #   Can call this root unless user is authenticated and a valid JWT token is passed

    def get_queryset(self):
        user = self.request.user    #   This gets the authenticated user
        return Note.objects.filter(author=user) #   Gets all the notes written by the authenticated user (User currently interacting with the page)
    
    # Once the serializer validates all the fields, it'll save/add the note
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)   #   Remeber author is read only we so it needs to be passed in here
        else:
            print(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user    #   This gets the authenticated user
        return Note.objects.filter(author=user)

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # Looks at all the objects for the create view so that we do not create one that already exists
    serializer_class = UserSerializer  #   Tells View what data to accept to create a new User
    permission_classes = [AllowAny] #   Allows anyone to use view to create new User
