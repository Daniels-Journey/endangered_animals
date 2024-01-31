from django.shortcuts import render
from django.views import View


class HomeView(View):
    HomeData = {
        "Title": "Home Page"

    }
    def get(self, request):
        return render(request, 'home.html', context=self.HomeData)


class SpeciesView(View):
    SpeciesData = {
        "Species": "Endangered Species List"

    }

    def get(self, request):
        return render(request, 'SpecList.html', context=self.SpeciesData)
