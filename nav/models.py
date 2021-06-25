from django.db import models
from content.models import AbstractModel

class Workspace(AbstractModel):
    dir_structure = models.JSONField(
        null = True,
        blank = True
    )
class DirTreeFolder(AbstractModel):
    parent_folder = models.ForeignKey(
        to = "nav.DirTreeFolder",
        blank = True,
        on_delete = models.CASCADE,
        default = 1
    )
    
class DirTreeFile(AbstractModel):
    extension = models.CharField(
        max_length = 500,
        null = True,
        blank = True
    )
    parent_folder = models.ForeignKey(
        to = "nav.DirTreeFolder",
        on_delete = models.CASCADE,
        blank = True
    )