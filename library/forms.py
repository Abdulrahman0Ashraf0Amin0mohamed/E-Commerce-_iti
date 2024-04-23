from django import  forms
from library.models import Library , Category , BorrowingModel

class CategoryForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    description = forms.CharField(label="description", max_length=100)



### create form ---> based on Model ?

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class SearchForm(forms.Form):
    id = forms.IntegerField(label='Enter ID')


