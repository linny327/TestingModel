from django.contrib import messages
from django.shortcuts import render
import pandas as pd
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from vitalsigns.forms import VitalsForm
from vitalsigns.models import VitalSigns
from vitalsigns.serializers import VitalSignsSerializers


class VitalSignsView(viewsets.ModelViewSet):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializers

# def vitals(request):
#     try:
#         pul = pd.read_csv("pulse.csv")
#         # Select the pulse_rate and cattle_gender columns from the DataFrame
#         x = pul[['pulse_rate', 'cattle_gender']]
#
#         calves = []
#         adults = []
#         abnormal = []
#         for index, row in pul.iterrows():
#             pulse_rate = float(row['pulse_rate'])
#             if pulse_rate >= 100 and pulse_rate <= 150:
#                 calves.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
#             elif pulse_rate >= 45 and pulse_rate <= 85:
#                 adults.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
#             else:
#                 abnormal.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
#         # print(calves)
#         # print(adults)
#         # print("abnornal ",abnormal)
#         for i in abnormal:
#             #return ('The likely disease a cattle is suffering from is {}'.format(predicted))
#             abnorn = " Cattle with id {0} has an abnormal pulse rate of {1}".format(i['cattle_id'], i['pulse_rate'])
#             print(abnorn)
#         return abnorn
#     except ValueError as e:
#         return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxvitals(request):
    if request.method == 'POST':
        form = VitalsForm(request.POST)
        if form.is_valid():
            vitals = form.cleaned_data['vitals']
            vitals1 = form.cleaned_data['vitals1']
            vitals2 = form.cleaned_data['vitals2']
            myData = {vitals, vitals1, vitals2}
        return myData
        pul = pd.read_csv("pulse.csv")
        # Select the pulse_rate and cattle_gender columns from the DataFrame
        x = pul[['pulse_rate', 'cattle_gender']]

        calves = []
        adults = []
        abnormal = []
        for index, row in pul.iterrows():
            pulse_rate = float(row['pulse_rate'])
            if pulse_rate >= 100 and pulse_rate <= 150:
                calves.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
            elif pulse_rate >= 45 and pulse_rate <= 85:
                adults.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
            else:
                abnormal.append({'cattle_id': row['cattle_id'], 'pulse_rate': row['pulse_rate']})
        # print(calves)
        # print(adults)
        # print("abnornal ",abnormal)
        for i in abnormal:
            # return ('The likely disease a cattle is suffering from is {}'.format(predicted))
            abnorn = " Cattle with id {0} has an abnormal pulse rate of {1}".format(i['cattle_id'], i['pulse_rate'])
            print(abnorn)
        # return abnorn
        messages.success(request, " Cattle with id {0} has an abnormal pulse rate of {1}".format(i['cattle_id'], i['pulse_rate']))
    form = VitalsForm()
    return render(request, 'myform/vitals.html', {'form': form})

