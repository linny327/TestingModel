import pandas as pd
import pickle
import joblib

df = pd.read_csv('CattleDiseases.csv')
print(df.columns)

pre_y = df['prognosis']
pre_X = df.drop('prognosis', axis=1)
dm_X = pd.get_dummies(pre_X)
#dm_y = pre_y.map(dict(Y=1, N=0))
#pre_y.shape
all_dm_col = dm_X.columns
print(dm_X.columns)

cat_columns=['lacrimation', 'abnormal_salivation', 'nasal_discharge', 'lameness',
            'firm_nodules_on_the_skin','enlarged_lymph_nodes', 'swollen_sore_legs', 'loss_of_appetite', 'eyes_nose_discharge', 'drop_in_milk',
            'weight_loss', 'blisters_in_mouth_and_feet','blisters_on_teats', 'dullness', 'shivering','rough_coat',
            'enlarged_parotid_gland','reluctant_to_move', 'anaemia', 'jaundice', 'severe_diarrhoea', 'swelling_in_the_neck',
            'cloudiness_of_the_eyes', 'breathing_difficulty', 'cyanosis_of_the_tongue', 'swelling_of_tongue_and_face']
df_processed = pd.get_dummies(pre_X, prefix_sep="_",columns=cat_columns)
print(df_processed)

joblib.dump(df_processed, 'encodedcolumns.pkl')
