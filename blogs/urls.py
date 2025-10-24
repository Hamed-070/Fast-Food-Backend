from django.urls import path, include
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import CustomUserView , FoodViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'foods' , FoodViewSet)


urlpatterns = [
    path('api/token/' , CustomUserView.as_view() , name="token_create") ,
    path('api/refresh/' , TokenRefreshView.as_view() , name="token_refresh") ,
    path('api/' , include(router.urls)) ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)