from django.urls import path
from .views import CurriculumAPIView, CurriculumDetailAPIView, EducationListCreateAPIView, EducationDetailAPIView, ExperienceListCreateAPIView, ExperienceDetailAPIView

urlpatterns = [
    path('curriculum/', CurriculumAPIView.as_view(), name='curriculum-list-create'),
    path('curriculum/<int:id>/', CurriculumDetailAPIView.as_view(), name='curriculum-detail'),
    path('education/', EducationListCreateAPIView.as_view(), name='education-list-create'),
    path('education/<int:pk>/', EducationDetailAPIView.as_view(), name='education-detail'),
    path('experience/', ExperienceListCreateAPIView.as_view(), name='experience-list-create'),
    path('experience/<int:pk>/', ExperienceDetailAPIView.as_view(), name='experience-detail'),
]
