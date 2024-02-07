from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from ConservationForum.models import Species, Post
from ConservationForum.forms import AddPostForm, SpeciesSearchForm, AlterSpeciesForm
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


class ForumView(ListView):

    model = Post
    template_name = 'Forum.html'
    context_object_name = 'forum_list'
    def get_queryset(self):
        return super().get_queryset()


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'AddPost.html'
    success_url = reverse_lazy('addPost')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlterSpecies(LoginRequiredMixin, UpdateView):
    model=Species
    form_class = AlterSpeciesForm
    template_name = 'AlterSpecies.html'
    success_url = reverse_lazy('specList')


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'DeletePost.html'  # Create a template for confirmation
    success_url = reverse_lazy('forum')  # Redirect to the forum or other page after deletion

    def get_object(self, queryset=None):
        # Override get_object to check if the user is the owner or a superuser
        obj = super().get_object(queryset)
        if not (obj.user == self.request.user or self.request.user.is_superuser):
            raise Http404("You don't have permission to delete this post.")
        return obj




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
