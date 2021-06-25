from django.db import models
from django.db.models import deletion
from django.db.models.deletion import DO_NOTHING
from django.db.models.enums import Choices
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
class AbstractDescModel(AbstractModel):
    description = models.CharField(
        max_length = 500,
        null = True,
        blank = True
    )

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
class AbstractVideoModel(AbstractModel):
    video_file = models.FileField(
        verbose_name = "Video File",
        null = True,
        blank = True
    )
    subtitle_transcription = models.JSONField(
        blank = True,
        null = True
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
    def __str__(self):
        return f"{self.title} (Parent Thread: {self.parent_thread})"

class Book(AbstractModel):
    description = models.CharField(
        max_length = 500, 
        null = True,
        blank = True
    )
class Chapter(AbstractDescModel):

    parent_book = models.ForeignKey(
        to = Book,
        on_delete = models.CASCADE
    )
class ChapterSection(AbstractDescModel):
    parent_chapter = models.ForeignKey(
        to = Chapter,
        on_delete = models.CASCADE
    )
class ChapterIntroQuote(AbstractDescModel):
    parent_chapter = models.ForeignKey(
        to = Chapter,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
class Paragraph(AbstractDescModel):
    body = models.CharField(
        max_length = 1000000,
        null = True,
        blank = True
    )
    parent_chapter_section = models.ForeignKey(
        to = ChapterSection,
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    parent_chapter = models.ForeignKey(
        null = True,
        blank = True,
        to = Chapter,
        on_delete = models.CASCADE
    )



#Video
class VideoContent(AbstractVideoModel):
    CHOICES = (
        ("Tutorial", "Tutorial"),
        ("Monologue", "Monologue"),
        ("Podcast", "Podcast"),
        ("Diagram Explanation", "Diagram Explanation")
    )
    type = models.CharField(
        max_length = 500,
        choices = CHOICES,
        null = True,
        blank  = True
    )
    def __str__(self):
        return f"{self.title} | {self.type}"