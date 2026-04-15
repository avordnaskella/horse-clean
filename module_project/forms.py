from django import forms
from .models import Category, Discipline

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['name', 'category', 'description', 'image', 'difficulty', 'is_olympic']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')
        if name and category:
            if Discipline.objects.filter(name=name, category=category).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Дисциплина с таким названием уже существует в данной категории.")
        return cleaned_data