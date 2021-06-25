from django.contrib import admin
from .models import DirTreeFile, DirTreeFolder, Workspace
# Register your models here.
models = [
    Workspace,
    DirTreeFolder,
    DirTreeFile
]
for model in models: 
    admin.site.register(model)