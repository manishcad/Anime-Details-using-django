from django import forms
from django.shortcuts import redirect, render
import requests
from django.conf import settings
from Anime_Details import settings
from django.conf.urls.static import static
from .models import Anime_Model
from .form import Anime_Form
from django.contrib import messages
# Create your views here.


def home(request):

    if request.method == "POST":
        global search
        search = request.POST.get("Anime_search")
        url = requests.get(
            f"https://kitsu.io/api/edge/anime?filter[text]={search}").json()

        data = url['data']

        try:
            if data[0]['attributes']['averageRating'] == None:
                return redirect('Home')

            context = {'name': data[0]['attributes']['slug'], }
            print(context['name'])
        except IndexError or TypeError:
            context = {'not_found': "Sorry No Matching result Found"}
            print("TYPE ERROR")
            return render(request, 'home.html', context)

        return redirect('anime_details')

    context = {}
    return render(request, 'home.html', context)


def details(request):
    global search
    print(search)
    url = requests.get(
        f"https://kitsu.io/api/edge/anime?filter[text]={search}").json()
    data = url['data']

    try:
        context = {

            'type': data[0]['type'],
            'name': data[0]['attributes']['slug'],
            'rating': data[0]['attributes']['averageRating'],
            'des': data[0]['attributes']['synopsis'],
            "start_date": data[0]['attributes']['startDate'],
            'end_date': data[0]['attributes']['endDate'],
            'status': data[0]['attributes']['status'],
            'image': data[0]['attributes']['posterImage']['medium'],
            'cover_image': data[0]['attributes']['coverImage']['large'],

        }
        print(context['cover_image'])
    except IndexError:
        context = {'not found': "No Matching Result Found"}

    return render(request, 'index.html', context)
