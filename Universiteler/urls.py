from django.urls import path
from . import views

urlpatterns = [
    path("", views.universiteler, name="universiteler"),
    path('universiteler/<int:uni_id>/', views.uni_fakulteler, name='uni_fakulteler'),
    path('fakulteler/<int:fakulte_id>/courses/', views.fakulte_bolumler, name='fakulte_courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('bolumler/<int:bolum_id>/courses/', views.bolum_courses, name='bolum_courses'), # Değişiklik burada
]