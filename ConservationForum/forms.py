from django import forms
from ConservationForum.models import Topic, Species

class CustomSpeciesChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        # Zmień sposób wyświetlania się species w formularzu
        return obj.name  # Wyświetl tylko nazwe gatunku

class PostForm(forms.Form):
    title = forms.ModelChoiceField(queryset=Topic.objects.all())
    text = forms.CharField(max_length=500)
    date = forms.DateField()
    species = CustomSpeciesChoiceField(Species.objects.all(),  widget=forms.CheckboxSelectMultiple)
    user_id = forms.IntegerField()