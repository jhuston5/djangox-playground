from django.urls import path
from .views import DrillCreateView, DrillDeleteView, DrillListView, DrillDetailView, DrillUpdateView, DrillUploadView

urlpatterns = [
  path('drills', DrillListView.as_view(), name='drill_list'),
  path('<int:pk>/', DrillDetailView.as_view(), name='drill_detail'),
  path('new/', DrillCreateView.as_view(), name='drill_create'),
  path('<int:pk>/edit', DrillUpdateView.as_view(), name='drill_update'),
  path('<int:pk>/delete', DrillDeleteView.as_view(), name='drill_delete'),
  path('upload/', DrillUploadView.as_view(), name='drill_upload'),
]