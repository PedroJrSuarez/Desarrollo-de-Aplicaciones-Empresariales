from django import forms


class LibroForm(forms.Form):
    """Formulario para crear y editar libros."""
    
    titulo = forms.CharField(
        label="Título",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese el título del libro'
        })
    )

    autor = forms.CharField(
        label="Autor",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese el nombre del autor'
        })
    )

    categoria = forms.CharField(
        label="Categoría",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ingrese la categoría'
        })
    )

    disponible = forms.BooleanField(
        label="Disponible",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox'
        })
    )
