from django.urls import path
from .views import VlogPostListView, VlogPostDetailView, VlogPostCreateView, VlogPostUpdateView

urlpatterns = [
    path('', VlogPostListView.as_view(), name='vlog_list'),  # Display all vlogs
    path('<int:id>/', VlogPostDetailView.as_view(), name='vlog-detail'),  # Display single vlog
    path('new/', VlogPostCreateView.as_view(), name='vlog-create'),  # Create new vlog
    path('edit/<int:id>/', VlogPostUpdateView.as_view(), name='vlog-edit'),  # Edit vlog
    path('create/', VlogPostCreateView.as_view(), name='vlog_create'),
]

