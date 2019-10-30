from django import forms


class PredictionForm(forms.Form):
    SYMPTOMS_CHOICES = (
        ('Choose A Symptom', 'Choose A Symptom'),
        ('lacrimation', 'lacrimation'),
        ('abnormal_salivation', 'abnormal_salivation'),
        ('nasal_discharge', 'nasal_discharge'),
        ('lameness', 'lameness'),
        ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
        ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'),
        ('swollen_sore_legs', 'swollen_sore_legs'),
        ('loss_of_appetite', 'loss_of_appetite'),
        ('eyes_nose_discharge', 'eyes_nose_discharge'),
        ('drop_in_milk', 'drop_in_milk'),
        ('weight_loss', 'weight_loss'),
        ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
        ('blisters_on_teats', 'blisters_on_teats'),
        ('dullness', 'dullness'),
        ('shivering', 'shivering'),
        ('rough_coat', 'rough_coat'),
        ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
        ('reluctant_to_move', 'reluctant_to_move'),
        ('anaemia', 'anaemia'),
        ('jaundice', 'jaundice'),
        ('severe_diarrhoea', 'severe_diarrhoea'),
        ('swelling_in_the_neck', 'swelling_in_the_neck'),
        ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
        ('breathing_difficulty', 'breathing_difficulty'),
        ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
        ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')
    )
    #category = forms.ChoiceField(choices=CHOICES)
    symptom1 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)
    symptom2 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)
    symptom3 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)
    symptom4 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)
    symptom5 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)
    symptom6 = forms.ChoiceField(choices=SYMPTOMS_CHOICES)


    # symptom1 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
    # symptom2 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
    # symptom3 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
    # symptom4 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
    # symptom5 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
    # symptom6 = forms.ChoiceField(
    #     choices=[('lacrimation', 'lacrimation'), ('abnormal_salivation', 'abnormal_salivation'),
    #              ('nasal_discharge', 'nasal_discharge'), ('lameness', 'lameness'),
    #              ('firm_nodules_on_the_skin', 'firm_nodules_on_the_skin'),
    #              ('enlarged_lymph_nodes', 'enlarged_lymph_nodes'), ('swollen_sore_legs', 'swollen_sore_legs'),
    #              ('loss_of_appetite', 'loss_of_appetite'), ('eyes_nose_discharge', 'eyes_nose_discharge'),
    #              ('drop_in_milk', 'drop_in_milk'),
    #              ('weight_loss', 'weight_loss'), ('blisters_in_mouth_and_feet', 'blisters_in_mouth_and_feet'),
    #              ('blisters_on_teats', 'blisters_on_teats'),
    #              ('dullness', 'dullness'), ('shivering', 'shivering'), ('rough_coat', 'rough_coat'),
    #              ('enlarged_parotid_gland', 'enlarged_parotid_gland'),
    #              ('reluctant_to_move', 'reluctant_to_move'), ('anaemia', 'anaemia'), ('jaundice', 'jaundice'),
    #              ('severe_diarrhoea', 'severe_diarrhoea'),
    #              ('swelling_in_the_neck', 'swelling_in_the_neck'), ('cloudiness_of_the_eyes', 'cloudiness_of_the_eyes'),
    #              ('breathing_difficulty', 'breathing_difficulty'), ('cyanosis_of_the_tongue', 'cyanosis_of_the_tongue'),
    #              ('swelling_of_tongue_and_face', 'swelling_of_tongue_and_face')])
