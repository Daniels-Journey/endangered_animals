from django.shortcuts import render, redirect
from django.views import View
from ConservationForum.models import Species, Post
from ConservationForum.forms import AddPostForm, SpeciesSearchForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

class HomeView(View):
    HomeData = {
        "Title": "Home Page"

    }
    def get(self, request):
        return render(request, 'home.html', context=self.HomeData)


class SpeciesView(ListView):

    model = Species
    template_name = 'SpecList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SpeciesSearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SpeciesSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            extinction_level = form.cleaned_data['extinction_level']
            queryset = queryset.filter(name__icontains=name)
            if extinction_level is not None:
                queryset = queryset.filter(extinction_level=extinction_level)
        return queryset


    # def get(self,request):
    #     species = Species.objects.all()
    #     form = SpeciesSearchForm(request.GET)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         species = species.filter(name__icontains=name)
    #
    #     return render(request, 'SpecList.html', context={'names':species, 'form': form})


class ForumView(View):
    def get(self, request):
        return render(request, 'Forum.html')


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'AddPost.html'
    success_url = reverse_lazy('addPost')


# class PostView(View):
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'AddPost.html', context={'postform':form})
#
#     def post(self,request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             textValid = form.cleaned_data['text']
#             dateValid = form.cleaned_data['date']
#             userValid = form.cleaned_data['user']
#             post = Post.objects.create(text=textValid, date=dateValid, user=userValid)
#             return redirect('addPost')
#
#         return render(request, 'AddPost.html', context={'postform': form})
