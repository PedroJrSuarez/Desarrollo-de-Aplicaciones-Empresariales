from django import forms

from .models import Asistencia, Cliente, Entrenador, Membresia, Rutina


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'fecha_registro']
        widgets = {'fecha_registro': forms.DateInput(attrs={'type': 'date'})}


class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre', 'apellido', 'especialidad', 'correo']


class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = ['tipo', 'fecha_inicio', 'fecha_fin', 'precio', 'activa']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('fecha_inicio')
        fin = cleaned_data.get('fecha_fin')
        if inicio and fin and fin < inicio:
            self.add_error('fecha_fin', 'La fecha final no puede ser anterior a la inicial.')
        return cleaned_data


class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ['nombre', 'descripcion', 'dias_semana', 'cliente', 'entrenador']


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['fecha', 'hora_entrada', 'observacion', 'cliente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
        }
