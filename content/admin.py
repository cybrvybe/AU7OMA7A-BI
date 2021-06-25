
from django.contrib import admin
from .models import Book, Chapter, ChapterIntroQuote, ChapterSection, Paragraph, Story, InstagramCarouselPage, InstagramCarousel, Tweet, TwitterThread, VideoContent

models = [
    Story,
    InstagramCarouselPage,
    InstagramCarousel,
    TwitterThread,
    Tweet,
    Book,
    Chapter,
    ChapterIntroQuote,
    ChapterSection,
    Paragraph,
    VideoContent
]
for model in models:
    admin.site.register(model)