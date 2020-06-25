from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.serializers import image, user, question, group_questions
from app.serializers import question_in_test, test, results
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'app'

urlpatterns = [
    path('users/', include(user.get_router_urls())),
    path('questions/', include(question.get_router_urls())),
    path('questions-in-tests/', include(question_in_test.get_router_urls())),
    path('group-questions/', include(group_questions.get_router_urls())),
    path('results/', include(results.get_router_urls())),
    path('tests/', include(test.get_router_urls())),
    path('images/', include(image.get_router_urls())),
    path('api/registration/', include('rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)