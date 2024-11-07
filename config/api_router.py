from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from catalyst_count.company.api.views import CompanyViewSet
from catalyst_count.users.api.views import UserViewSet
from django.urls import path
from catalyst_count.company import views
from django.views.generic import TemplateView

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet)


app_name = "api"
urlpatterns =[
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('upload_data/', views.UploadDataView.as_view(), name='upload_data'),
] + router.urls 
