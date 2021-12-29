from django.urls import path
from .views import (home_view, reports_view, csv_upload_view, UploadTemplateView)

app_name= 'reports'

urlpatterns = [
    path('', home_view, name='home'),
    path('reports/', reports_view, name='reports'),
    path('upload/', csv_upload_view, name='upload'),
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
]
