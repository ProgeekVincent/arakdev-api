from django.urls import path
from .views import ContactCreateView, ResumeLeadCreateView, ResumeDownloadView

urlpatterns = [
    path("contact/", ContactCreateView.as_view()),
    path("resume/request/", ResumeLeadCreateView.as_view()),
    path("resume/download/<uuid:token>/", ResumeDownloadView.as_view()),
]