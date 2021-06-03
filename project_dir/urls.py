"""project_dir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from general_business import views as general_business_views

router = routers.DefaultRouter()
router_item_list = [
    {
        "plural": r"organizations",
        "view": general_business_views.OrganizationView,
        "singular": "organization"
    }
]

for router_item in router_item_list:
    router.register(
        router_item["plural"],
        router_item["view"],
        router_item["singular"]
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/",
        include(router.urls)
    )
]
