from django.forms import ModelForm
from .models import Alzhimer

class MyForm(ModelForm):
	class Meta:
		model=Alzhimer
		fields = '__all__'