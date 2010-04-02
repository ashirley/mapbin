# Create your views here.
from mapbin.gmlStore.models import Annotation
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
import datetime

#normal web 1.0 views

def index(request):
    return HttpResponse("You're looking at gml index.")

def info(request, gml_id):
    return render_to_response('gmlStore/info.html', {'gml_id': gml_id})


# AJAX views

def get(request, gml_id):
    annotation = get_object_or_404(Annotation, pk=gml_id)
    return HttpResponse(annotation.gml, mimetype="text/xml")

def store(request):
    #TODO: fail gracefully if this isn't a post with the right fields.
    annotation = Annotation(gml=request.POST['gml'], creation_date=datetime.now())
    annotation.save()
    return HttpResponse(("<stored id='%s' />" % (annotation.id)), mimetype="text/xml")

