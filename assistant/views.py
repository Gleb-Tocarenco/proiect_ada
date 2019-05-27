from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def image_view(request):
	return JsonResponse({"message": "ok"})

@csrf_exempt
def text_view(request):
	return JsonResponse({"message": "ok"})