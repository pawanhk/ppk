from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Home View

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')