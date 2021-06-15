
from django.contrib import admin
from .models import Book, Chapter, ChapterIntroQuote, ChapterSection, Paragraph, Story, InstagramCarouselPage, InstagramCarousel, Tweet, TwitterThread

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
    Paragraph
]
for model in models:
    admin.site.register(model)