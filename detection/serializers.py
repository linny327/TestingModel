from rest_framework import serializers
from . models import Predictions

#handles requests and convert it into json in background
class PredictionsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Predictions
		fields='__all__'

