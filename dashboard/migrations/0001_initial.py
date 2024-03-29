# Generated by Django 2.2.5 on 2019-10-29 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblBreed',
            fields=[
                ('idtbl_breed', models.AutoField(db_column='idtbl_Breed', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_breed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattle',
            fields=[
                ('idtbl_cattle', models.AutoField(db_column='idtbl_Cattle', primary_key=True, serialize=False)),
                ('date_of_birth', models.CharField(db_column='Date_of_birth', max_length=45)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
            ],
            options={
                'db_table': 'tbl_cattle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleDesease',
            fields=[
                ('idtbl_cattle_desease', models.AutoField(db_column='idtbl_Cattle_Desease', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'tbl_cattle_desease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleGender',
            fields=[
                ('idtbl_cattle_gender', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_cattle_gender',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCause',
            fields=[
                ('idtbl_cause', models.AutoField(primary_key=True, serialize=False)),
                ('desciption', models.CharField(db_column='Desciption', max_length=45)),
            ],
            options={
                'db_table': 'tbl_cause',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblDetection',
            fields=[
                ('idtbl_detection', models.AutoField(db_column='idtbl_Detection', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('extent', models.CharField(db_column='Extent', max_length=45)),
                ('affected_prdediction', models.IntegerField(db_column='Affected_prdediction')),
                ('solved', models.IntegerField(blank=True, db_column='Solved', null=True)),
            ],
            options={
                'db_table': 'tbl_detection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblDiseaseSysmptom',
            fields=[
                ('idtbl_disease_sysmptom', models.AutoField(db_column='idtbl_Disease_sysmptom', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_disease_sysmptom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblDrug',
            fields=[
                ('idtbl_drug', models.AutoField(db_column='idtbl_Drug', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'tbl_drug',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblFarm',
            fields=[
                ('idtbl_farm', models.AutoField(db_column='idtbl_Farm', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=200)),
                ('size', models.CharField(db_column='Size', max_length=45)),
            ],
            options={
                'db_table': 'tbl_farm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblFarmingRegion',
            fields=[
                ('idtbl_farming_region', models.AutoField(db_column='idtbl_Farming_region', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
                ('temperature_min', models.FloatField(db_column='Temperature_min')),
                ('temperature_max', models.FloatField(db_column='Temperature_max')),
                ('rainfall_min', models.FloatField(db_column='Rainfall_min')),
                ('rainfall_max', models.FloatField(db_column='Rainfall_max')),
            ],
            options={
                'db_table': 'tbl_farming_region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblGender',
            fields=[
                ('idtbl_gender', models.AutoField(db_column='idtbl_Gender', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_gender',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblHeard',
            fields=[
                ('idtbl_heard', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_heard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLogin',
            fields=[
                ('idtbl_login', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=45, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'tbl_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblNormalSign',
            fields=[
                ('idtbl_normal_sign', models.AutoField(db_column='idtbl_Normal_Sign', primary_key=True, serialize=False)),
                ('feed_min', models.FloatField(db_column='Feed_min')),
                ('feed_max', models.FloatField(db_column='Feed_max')),
                ('water_min', models.FloatField(db_column='Water_min')),
                ('water_max', models.FloatField(db_column='Water_max')),
                ('temparature_min', models.FloatField(db_column='Temparature_min')),
                ('temperature_max', models.FloatField(db_column='Temperature_max')),
                ('respiration_min', models.FloatField(db_column='Respiration_min')),
                ('respiration_max', models.FloatField(db_column='Respiration_max')),
                ('pulse_max', models.IntegerField(db_column='Pulse_max')),
                ('pulse_min', models.IntegerField(db_column='Pulse_min')),
            ],
            options={
                'db_table': 'tbl_normal_sign',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblNotifications',
            fields=[
                ('idtbl_notifications', models.AutoField(db_column='idtbl_Notifications', primary_key=True, serialize=False)),
                ('message', models.CharField(db_column='Message', max_length=45)),
                ('submission_date', models.CharField(db_column='Submission_date', max_length=45)),
                ('read', models.IntegerField(db_column='Read')),
                ('broadcasted', models.IntegerField(db_column='Broadcasted')),
            ],
            options={
                'db_table': 'tbl_notifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblReadings',
            fields=[
                ('idtbl_readings', models.AutoField(primary_key=True, serialize=False)),
                ('tempareture', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_readings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblSeason',
            fields=[
                ('idtbl_season', models.AutoField(db_column='idtbl_Season', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
                ('starting_month', models.CharField(db_column='Starting_month', max_length=45)),
                ('ending_month', models.CharField(db_column='Ending_month', max_length=45)),
            ],
            options={
                'db_table': 'tbl_season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblStatus',
            fields=[
                ('idtbl_status', models.AutoField(db_column='idtbl_Status', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45)),
            ],
            options={
                'db_table': 'tbl_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblUser',
            fields=[
                ('idtbl_user', models.AutoField(db_column='idtbl_User', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='First_name', max_length=100)),
                ('other_name', models.CharField(blank=True, db_column='Other_name', max_length=100, null=True)),
                ('surname', models.CharField(db_column='Surname', max_length=100)),
                ('date_of_birth', models.DateField(db_column='Date_of_birth')),
                ('email_address', models.CharField(db_column='Email_address', max_length=200)),
                ('mobile_number', models.CharField(db_column='Mobile_number', max_length=45)),
            ],
            options={
                'db_table': 'tbl_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblUserLevel',
            fields=[
                ('idtbl_user_level', models.AutoField(db_column='idtbl_User_level', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'tbl_user_level',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblBreedHasTblSeason',
            fields=[
                ('tbl_breed_idtbl_breed', models.ForeignKey(db_column='tbl_Breed_idtbl_Breed', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblBreed')),
            ],
            options={
                'db_table': 'tbl_breed_has_tbl_season',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleDeseaseHasTblCause',
            fields=[
                ('tbl_cattle_desease_idtbl_cattle_desease', models.ForeignKey(db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblCattleDesease')),
            ],
            options={
                'db_table': 'tbl_cattle_desease_has_tbl_cause',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleDeseaseHasTblDetection',
            fields=[
                ('tbl_cattle_desease_idtbl_cattle_desease', models.ForeignKey(db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblCattleDesease')),
            ],
            options={
                'db_table': 'tbl_cattle_desease_has_tbl_detection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleDeseaseHasTblDiseaseSysmptom',
            fields=[
                ('tbl_cattle_desease_idtbl_cattle_desease', models.ForeignKey(db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblCattleDesease')),
            ],
            options={
                'db_table': 'tbl_cattle_desease_has_tbl_disease_sysmptom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblCattleDeseaseHasTblDrug',
            fields=[
                ('tbl_cattle_desease_idtbl_cattle_desease', models.ForeignKey(db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblCattleDesease')),
                ('duration_days_field', models.IntegerField(db_column='Duration(Days)')),
            ],
            options={
                'db_table': 'tbl_cattle_desease_has_tbl_drug',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblDetectionHasTblCattle',
            fields=[
                ('tbl_detection_idtbl_detection', models.ForeignKey(db_column='tbl_Detection_idtbl_Detection', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblDetection')),
            ],
            options={
                'db_table': 'tbl_detection_has_tbl_cattle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblFarmingRegionHasTblCattleDesease',
            fields=[
                ('tbl_farming_region_idtbl_farming_region', models.ForeignKey(db_column='tbl_Farming_region_idtbl_Farming_region', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.TblFarmingRegion')),
            ],
            options={
                'db_table': 'tbl_farming_region_has_tbl_cattle_desease',
                'managed': False,
            },
        ),
    ]
