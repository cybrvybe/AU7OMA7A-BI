from django.contrib import admin
from .models import Brand, Campaign, SocialMediaAccount
# Register your models here.
models = [
    Campaign,
    SocialMediaAccount,
    Brand
]

for model in models: 
    admin.site.register(model)