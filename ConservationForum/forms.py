from django import forms
from django.contrib.auth.models import User

from ConservationForum.models import Topic, Species, Post, ExtinctionLevel

# Inny zapis
# class PostForm(forms.Form):
#     title = forms.ModelChoiceField(queryset=Topic.objects.all())
#     text = forms.CharField(max_length=500)
#     date = forms.DateField()
#     species = forms.ModelChoiceField(Species.objects.all(),  widget=forms.CheckboxSelectMultiple)
#     user_id = forms.IntegerField()


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'species': forms.CheckboxSelectMultiple()
        }

    def __init__(self, user, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        self.fields['user'].queryset = User.objects.filter(pk=user.pk)

class SpeciesSearchForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    # population = forms.IntegerField(required=False)
    extinction_level = forms.ModelChoiceField(queryset=ExtinctionLevel.objects.all(), required=False)


class AlterSpeciesForm(forms.ModelForm):

    class Meta:
        model = Species
        fields = '__all__'


