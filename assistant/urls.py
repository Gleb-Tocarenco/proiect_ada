from django.urls import path
from . import views

urlpatterns = (
	path('image/', views.image_view),
	path('text/', views.text_view)
)