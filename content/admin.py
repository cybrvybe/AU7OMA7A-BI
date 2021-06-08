
from django.contrib import admin
from .models import Story, InstagramCarouselPage, InstagramCarousel, Tweet, TwitterThread

models = [
    Story,
    InstagramCarouselPage,
    InstagramCarousel,
    TwitterThread,
    Tweet
]
for model in models:
    admin.site.register(model)