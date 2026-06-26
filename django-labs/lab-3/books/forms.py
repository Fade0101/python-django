from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Include fields the user fills out manually
        fields = ['title', 'desc', 'rate', 'categories']
        
        # This adds styling classes so your HTML looks neat
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5}),
            'categories': forms.CheckboxSelectMultiple(),  # Handles the Many-to-Many selection nicely
        }

    # Custom clean method for title length validation (Requirement 7.1)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10 or len(title) > 50:
            raise forms.ValidationError("The length of a book title must be between 10 & 50 characters.")
        return title