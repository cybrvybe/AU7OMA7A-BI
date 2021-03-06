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
from budgeting import views as budgeting_views
from career import views as career_views
from marketing import views as marketing_views
from processes import views as process_views
from product import views as product_views
from project import views as project_views
from modules import views as module_views
from nav import views as nav_views
from analytics import views as bot_views
from content import views as content_views

router = routers.DefaultRouter()
router_item_list = [
    {
        "plural": r"organizations",
        "view": general_business_views.OrganizationView,
        "singular": "organization"
    },
    {
        "plural": r"ventures",
        "view": general_business_views.VentureView,
        "singular": "venture"
    },
    {
        "plural": r"roles",
        "view": general_business_views.RoleView,
        "singular": "role"
    },
    {
        "plural": r"budgets",
        "view": budgeting_views.BudgetView,
        "singular": "budget"
    },
    {
        "plural": r"expenses",
        "view": budgeting_views.ExpenseView,
        "singular": "expense"
    },
    {
        "plural": r"income_streams",
        "view": budgeting_views.IncomeStreamView,
        "singular": "income_stream"
    },
    {
        "plural": r"income_events",
        "view": budgeting_views.IncomeEventView,
        "singular": "income_event"
    },
    {
        "plural":r"companies",
        "view": career_views.CompanyView,
        "singular": "company"
    },
    {
        "plural": r"career_contacts",
        "view": career_views.CareerContactView,
        "singular": "career_contact"
    },
    {
        "plural": r"career_roles",
        "view": career_views.CareerRoleView,
        "singular": "career_role"
    },
    {
        "plural": r"campaigns",
        "view": marketing_views.CampaignView,
        "singular": "campaign"
    },
    {
        "plural": r"brands",
        "view": marketing_views.BrandView,
        "singular": "brand"
    },
    {
        "plural": r"social_media_accounts",
        "view": marketing_views.SocialMediaAccountView,
        "singular": "social_media_account"
    },
    {
        "plural": r"processes",
        "view": process_views.ProcessView,
        "singular": "process"
    },
    {
        "plural": r"products",
        "view": product_views.ProductView,
        "singular": "product"
    },
    {
        "plural": r"services",
        "view": product_views.ServiceView,
        "singular": "service"
    },
    {
        "plural": r"projects",
        "view": project_views.ProjectView,
        "singular": "project"

    },
    {
        "plural": r"features",
        "view": project_views.FeatureView,
        "singular": "feature"
    },
    {
        "plural": r"modules",
        "view": module_views.ModuleView,
        "singular": "module"
    },
    {
        "plural": r"workspaces",
        "view": nav_views.WorkspaceView,
        "singular": "workspace"
    },
    {
        "plural": r"dir_tree_folders",
        "view": nav_views.DirTreeFolderView,
        "singular": "dir_tree_folder"
    },
    {
        "plural": r"bots",
        "view": bot_views.BotView,
        "singular": "bot"
    },
    {
        "plural": r"videos_content",
        "view": content_views.VideoContentView,
        "singular": "video_content"
    },
    {
        "plural": r"techs",
        "view": project_views.TechView,
        "singular": "tech"
    },
    {
        "plural": r"tasks",
        "view": project_views.TaskView,
        "singular": "task"
    }
    
]
bot_router_item_list = [
    {
        "plural": "expense_time_interval_cost_breakdowns",
        "view": budgeting_views.ExpenseTimeIntervalCostBreakdownView,
        "singular": "expense_time_interval_cost_breakdown"

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
for view in bot_router_item_list:
    new_path = path(
        "api/" + view["plural"] + "/",
        view["view"].as_view(),
        name = view["singular"]

    )
    urlpatterns.append(new_path)
