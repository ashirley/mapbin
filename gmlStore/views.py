# Create your views here.
from mapbin.gmlStore.models import Annotation
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("You're looking at gml index.")

def get(request, gml_id):
    annotation = get_object_or_404(Annotation, pk=gml_id)
    output = annotation.gml
    return HttpResponse(output)

def info(request, gml_id):
    return HttpResponse("You're looking at gml %s." % gml_id)
