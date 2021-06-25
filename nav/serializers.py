from rest_framework import serializers
from .models import DirTreeFile, Workspace, DirTreeFolder

class WorkspaceSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Workspace
        fields = [
            "title",
            "created_at",
            "dir_structure"
        ]
class DirTreeFolderSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = DirTreeFolder
        fields = [
            "title",
            "created_at",
            "parent_folder"
        ]
class DirTreeFileSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = DirTreeFile
        fields = [
            "title",
            "created_at",
            "extension",
            "parent_folder"
        ]
