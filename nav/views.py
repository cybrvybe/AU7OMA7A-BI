from django.shortcuts import render
from rest_framework import viewsets
from .models import DirTreeFile, DirTreeFolder, Workspace
from .serializers import DirTreeFileSerializer, DirTreeFolderSerializer, WorkspaceSerializer
# Create your views here.

class WorkspaceView(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
    
class DirTreeFolderView(viewsets.ModelViewSet):
    serializer_class = DirTreeFolderSerializer
    queryset = DirTreeFolder.objects.all()

class DirTreeFileView(viewsets.ModelViewSet):
    serializer_class = DirTreeFileSerializer
    queryset = DirTreeFile.objects.all()