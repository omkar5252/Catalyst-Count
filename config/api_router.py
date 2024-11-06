from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from catalyst_count.company.api.views import CompanyViewSet
from catalyst_count.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet)


app_name = "api"
urlpatterns = router.urls
