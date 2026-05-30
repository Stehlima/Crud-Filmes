from django import forms
from .models import Filme, Categoria

class FilmeForm(forms.ModelForm):
    nova_categoria = forms.CharField(max_length=100, required=False, help_text="Ou digite uma nova categoria")

    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'ano_lancamento', 'categoria', 'capa', 'capa_url']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_titulo'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_diretor'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_ano_lancamento'}),
            'categoria': forms.Select(attrs={'class': 'form-select', 'id': 'id_categoria'}),
            'capa': forms.FileInput(attrs={'class': 'form-control', 'id': 'id_capa'}),
            'capa_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'id_capa_url', 'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        nova_categoria = cleaned_data.get('nova_categoria')

        if not categoria and not nova_categoria:
            raise forms.ValidationError("Você deve selecionar uma categoria existente ou criar uma nova.")
            
        if nova_categoria:
            cat, created = Categoria.objects.get_or_create(nome=nova_categoria.title())
            cleaned_data['categoria'] = cat
            
        return cleaned_data
