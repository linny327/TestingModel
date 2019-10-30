from .forms import PredictionForm
from django.shortcuts import render
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.externals import joblib
from sklearn.preprocessing import RobustScaler
from .models import Predictions
from .serializers import PredictionsSerializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import datetime

# Create your views here.
class PredictionsView(viewsets.ModelViewSet):
    queryset = Predictions.objects.all()
    serializer_class = PredictionsSerializers



model = joblib.load("/Users/Linny/PycharmProjects/TestingModel/detection/model.pkl")
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def approvereject(request):
    try:
        # data = request.data

        model = joblib.load("/Users/Linny/PycharmProjects/TestingModel/detection/model.pkl")
        user_input = {'rise_in_temperature':0, 'fever':0,'lacrimation': 0, 'abnormal_salivation': 0, 'nasal_discharge': 0, 'lameness': 0,
                      'firm_nodules_on_the_skin': 0,
                      'enlarged_lymph_nodes': 0, 'swollen_sore_legs': 0, 'loss_of_appetite': 0,
                      'eyes_nose_discharge': 0,
                      'drop_in_milk': 0,
                      'weight_loss': 0, 'blisters_in_mouth_and_feet': 0, 'blisters_on_teats': 0, 'dullness': 0,
                      'shivering': 0,
                      'rough_coat': 0,
                      'enlarged_parotid_gland': 0, 'increased_respiratory_rate':0,'reluctant_to_move': 0, 'anaemia': 0, 'jaundice': 0,
                      'severe_diarrhoea': 0,
                      'swelling_in_the_neck': 0,
                      'cloudiness_of_the_eyes': 0, 'breathing_difficulty': 0, 'cyanosis_of_the_tongue': 0,
                      'swelling_of_tongue_and_face': 0}

        def input_to_one_hot(data):
            # initialize the target vector with zero values
            enc_input = np.zeros(29)
            # set the numerical input as they are

            enc_input[0] = data['rise_in_temperature']
            enc_input[1] = data['fever']
            enc_input[2] = data['lacrimation']
            enc_input[3] = data['abnormal_salivation']
            enc_input[4] = data['nasal_discharge']
            enc_input[5] = data['lameness']
            enc_input[6] = data['firm_nodules_on_the_skin']
            enc_input[7] = data['enlarged_lymph_nodes']
            enc_input[8] = data['swollen_sore_legs']
            enc_input[9] = data['loss_of_appetite']
            enc_input[10] = data['eyes_nose_discharge']
            enc_input[11] = data['drop_in_milk']
            enc_input[12] = data['weight_loss']
            enc_input[13] = data['blisters_in_mouth_and_feet']
            enc_input[14] = data['blisters_on_teats']
            enc_input[15] = data['dullness']
            enc_input[16] = data['shivering']
            enc_input[17] = data['rough_coat']
            enc_input[18] = data['enlarged_parotid_gland']
            enc_input[19] = data['increased_respiratory_rate']
            enc_input[20] = data['reluctant_to_move']
            enc_input[21] = data['anaemia']
            enc_input[22] = data['jaundice']
            enc_input[23] = data['severe_diarrhoea']
            enc_input[24] = data['swelling_in_the_neck']
            enc_input[25] = data['cloudiness_of_the_eyes']
            enc_input[26] = data['breathing_difficulty']
            enc_input[27] = data['cyanosis_of_the_tongue']
            enc_input[28] = data['swelling_of_tongue_and_face']

            return enc_input

        a = input_to_one_hot(user_input)
        pred = model.predict([a])
        predicted = pred[0]
        #response = {'pred': predicted}
        #return JsonResponse(response)
        return ('The likely disease a cattle is suffering from is {}'.format(predicted))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


# defining farmer form to check if the cow is sick
def cxcontact(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            symptom1 = form.cleaned_data['symptom1']
            symptom2 = form.cleaned_data['symptom2']
            symptom3 = form.cleaned_data['symptom3']
            symptom4 = form.cleaned_data['symptom4']
            symptom5 = form.cleaned_data['symptom5']
            #symptom6 = form.cleaned_data['symptom6']
            myData = {symptom1, symptom2, symptom3, symptom4, symptom5}

            symptoms = {}
            for symptom in myData:
                if symptom not in symptoms:
                    symptoms[symptom] = 1

            def input_to_one_hot(data):
                # initialize the target vector with zero values
                enc_input = np.zeros(29)

                s_list = ['rise_in_temperature', 'fever','lacrimation','abnormal_salivation', 'nasal_discharge', 'lameness',
                               'firm_nodules_on_the_skin',
                               'enlarged_lymph_nodes', 'swollen_sore_legs', 'loss_of_appetite',
                               'eyes_nose_discharge',
                               'drop_in_milk',
                               'weight_loss', 'blisters_in_mouth_and_feet', 'blisters_on_teats', 'dullness',
                               'shivering',
                               'rough_coat',
                               'enlarged_parotid_gland', 'increased_respiratory_rate', 'reluctant_to_move', 'anaemia', 'jaundice',
                               'severe_diarrhoea',
                               'swelling_in_the_neck',
                               'cloudiness_of_the_eyes', 'breathing_difficulty', 'cyanosis_of_the_tongue',
                               'swelling_of_tongue_and_face']

                for smpy in data:
                    enc_input[s_list.index(smpy)] = data[smpy]

                return enc_input

            a = input_to_one_hot(symptoms)
            pred = model.predict([a])
            predicted = pred[0]
            print(predicted)
            messages.success(request, 'The likely disease a cattle is suffering from is {}'.format(predicted))
            #print( 'The likely disease is: {}'.format(predicted))
            #return ('The likely disease a cattle is suffering from is {}'.format(predicted))
    form = PredictionForm()
    return render(request, 'myform/cxform.html', {'form': form})


