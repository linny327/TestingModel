from django.forms import Textarea
from rest_framework import serializers
from . models import VitalSigns

#handles requests and convert it into json in background
class VitalSignsSerializers(serializers.ModelSerializer):
	class Meta:
		model=VitalSigns
		fields='__all__'
		widgets = {
			'vitals': Textarea(attrs={'cols': 80, 'rows': 20}),
			'vitals1': Textarea(attrs={'cols': 80, 'rows': 20}),
			'vitals2': Textarea(attrs={'cols': 80, 'rows': 20}),
		}

