from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def dbMngt(request, resource):
    if request.method == "GET":
        try:
            page = Pages.objects.get(name = resource)
            return HttpResponse(page.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Page " + resource + " is not available")
    if request.method == "PUT":
        newPage = Pages(name = resource, page = "Pagina de " + request.body)
        newPage.save()
        return HttpResponse("Page " + request.body + " successfully saved")
