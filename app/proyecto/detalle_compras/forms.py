from django import forms
from detalle_compras.models import Detalle_compra,Compra,Proveedor,Articulo,Marca

class Form_detalle_compra(forms.ModelForm):
    class Meta:
        model=Detalle_compra
        #fields=['nombre','genero','stock']
        fields='__all__'

class Form_compra(forms.ModelForm):
    class Meta:
        model=Compra
        #fields=['nombre','genero','stock']
        fields='__all__'

class Form_proveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        #fields=['nombre','genero','stock']
        fields='__all__'

class Form_articulo(forms.ModelForm):
    class Meta:
        model=Articulo
        #fields=['nombre','genero','stock']
        fields='__all__'

class Form_marca(forms.ModelForm):
    class Meta:
        model=Marca
        #fields=['nombre','genero','stock']
        fields='__all__'