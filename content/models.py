from django.db import models
from django.db.models.deletion import DO_NOTHING
from marketing.models import SocialMediaAccount
from datetime import datetime
#####################################################
#abstract  models
######################################################
class AbstractModel(models.Model):
    title = models.CharField(
        max_length = 500,
        null = True,
        blank = True,
        default = "default title"
    )
    created_at = models.DateTimeField(
        auto_now = True
    )
    #sets this models state, such that Django recognizes it as an abstract model.
    class Meta:
        abstract = True

    #formats the object display name so it displays nicely in the django admin. 
    def __str__(self):
        return f"{self.title}"
        
class AbstractImgModel(AbstractModel):
    png_file = models.FileField(
        verbose_name = "PNG file",
        null = True,
        blank = True
    )
    svg_file = models.FileField(
        verbose_name = "SVG file",
        null = True,
        blank = True
    )

class AbstractAudioModel(AbstractModel):
    mp3_file = models.FileField(
        verbose_name = "MP3 file",
        null = True,
        blank = True
    )
    wav_file = models.FileField(
        verbose_name = "WAV file",
        null = True,
        blank = True
    )
####################################

######################################
class InstagramCarousel(AbstractImgModel):
    count = models.IntegerField(
        verbose_name = "Page Count"
    )
    def __str__(self):
        return f"{self.title}, {self.count}"

class InstagramCarouselPage(AbstractImgModel):
    parent_carousel = models.ForeignKey(
        to =  InstagramCarousel,
        on_delete = models.DO_NOTHING
    )
class Story(AbstractModel):
    content_file = models.FileField(
        verbose_name = "What is the file playing in the background of this story?",
        null = True,
        blank = True
    )
    poll_question =  models.CharField(
        max_length = 500,
        null = True,
        blank = True
    )
    social_account = models.ForeignKey(
        to = SocialMediaAccount,
        on_delete = models.DO_NOTHING
    )
class TwitterThread(AbstractModel):
    null_value = None
class Tweet(AbstractModel):
    img_file = models.FileField(
        verbose_name = "Image File",
        null = True,
        blank = True
    )
    content_text = models.CharField(
        max_length = 250,
        null = True,
        blank = True
        )
    date_uploaded = models.DateTimeField(
        auto_now = True
    )
    parent_thread = models.ForeignKey(
        to = TwitterThread,
        on_delete = models.DO_NOTHING
    )

   