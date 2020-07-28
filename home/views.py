from django.shortcuts import render
from django.views.generic.base import View

from .models import Pets

class PetView(View):
	def get(self, request):
		pets = Pets.objects.all()
		return render (request, "home/pets.html", {'pet_list': pets})