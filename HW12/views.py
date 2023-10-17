from django.http import HttpResponse
from .models import ExampleModel

def home(request):
    return HttpResponse("Добро пожаловать на домашнюю страницу!")

def get_specific_columns(request):
    entries = ExampleModel.objects.values('name')
    return HttpResponse("Response for get_columns")


def exclude_specific_values(request):
    entries = ExampleModel.objects.exclude(name='unwanted_name')
    return HttpResponse("Response for exclude_values")

