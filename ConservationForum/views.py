from django.shortcuts import render, redirect
from django.views import View
from ConservationForum.models import Species, ExtinctionLevel
from ConservationForum.forms import PostForm

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
        lst = Species.objects.all()
        return render(request, 'SpecList.html', context={'names':lst})


class ForumView(View):
    def get(self, request):
        return render(request, 'Forum.html')


class PostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'AddPost.html', context={'postform':form})

    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data['name']
            extinctionlvl = ExtinctionLevel.objects.create(name=names)
            return redirect('addPost')

        return render(request, 'AddPost.html', context={'postform': form})