from django.shortcuts import render
# Create your views here.
from django.views import View
from .models import Person
from django.http import JsonResponse
from django.forms.models import model_to_dict

class PersonListView(View):
    def get(self, request):
        if ('name' in request.GET):
            clist = Person.objects.filter(name__contains = request.GET['name'])
        else:
        # get
            clist = Person.objects.all()
        return JsonResponse(list(clist.values()), safe = False)

class StateListView(View):
    def get(self, request):
        if ('state_place' in request.GET):
            cclist = Person.objects.filter(name__contains = request.GET['state_place'])
        else:
        # get
            cclist = Person.objects.all()
        return JsonResponse(list(cclist.values()), safe = False)


class PersonDetailView(View):
    def get(self, request, pk):
        # get
        cdetail = Person.objects.get(pk = pk)
        return JsonResponse(model_to_dict (cdetail))
