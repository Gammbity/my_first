from django import forms
from .models import TodoModel

class CreateTodoModelForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        fields = ['task_name', 'task_description']
        
class EditTodoModelForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        exclude = ['task_name','task_description']        