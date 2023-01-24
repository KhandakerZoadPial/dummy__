from django import forms
# Models
from quality_control.models import Questions

class NewQuestionForm(forms.ModelForm):
    question = forms.CharField(required=True)
   
    class Meta:
        model = Questions
        fields = ('__all__')