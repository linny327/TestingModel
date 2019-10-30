from django.db import models

# Create your models here.
class TblBreed(models.Model):
    idtbl_breed = models.AutoField(db_column='idtbl_Breed', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    tbl_normal_sign_idtbl_normal_sign = models.ForeignKey('TblNormalSign', models.DO_NOTHING, db_column='tbl_Normal_Sign_idtbl_Normal_Sign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_breed'


class TblBreedHasTblSeason(models.Model):
    tbl_breed_idtbl_breed = models.ForeignKey(TblBreed, models.DO_NOTHING, db_column='tbl_Breed_idtbl_Breed', primary_key=True)  # Field name made lowercase.
    tbl_season_idtbl_season = models.ForeignKey('TblSeason', models.DO_NOTHING, db_column='tbl_Season_idtbl_Season')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_breed_has_tbl_season'
        unique_together = (('tbl_breed_idtbl_breed', 'tbl_season_idtbl_season'),)


class TblCattle(models.Model):
    idtbl_cattle = models.AutoField(db_column='idtbl_Cattle', primary_key=True)  # Field name made lowercase.
    date_of_birth = models.CharField(db_column='Date_of_birth', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tbl_status_idtbl_status = models.ForeignKey('TblStatus', models.DO_NOTHING, db_column='tbl_Status_idtbl_Status')  # Field name made lowercase.
    tbl_heard_idtbl_heard = models.ForeignKey('TblHeard', models.DO_NOTHING, db_column='tbl_heard_idtbl_heard')
    tbl_normal_sign_idtbl_normal_sign = models.ForeignKey('TblNormalSign', models.DO_NOTHING, db_column='tbl_Normal_Sign_idtbl_Normal_Sign')  # Field name made lowercase.
    tbl_cattle_gender_idtbl_cattle_gender = models.ForeignKey('TblCattleGender', models.DO_NOTHING, db_column='tbl_cattle_gender_idtbl_cattle_gender')

    class Meta:
        managed = False
        db_table = 'tbl_cattle'


class TblCattleDesease(models.Model):
    idtbl_cattle_desease = models.AutoField(db_column='idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease'


class TblCattleDeseaseHasTblCause(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_cause_idtbl_cause = models.ForeignKey('TblCause', models.DO_NOTHING, db_column='tbl_cause_idtbl_cause')

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_cause'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_cause_idtbl_cause'),)


class TblCattleDeseaseHasTblDetection(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_detection_idtbl_detection = models.ForeignKey('TblDetection', models.DO_NOTHING, db_column='tbl_Detection_idtbl_Detection')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_detection'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_detection_idtbl_detection'),)


class TblCattleDeseaseHasTblDiseaseSysmptom(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_disease_sysmptom_idtbl_disease_sysmptom = models.ForeignKey('TblDiseaseSysmptom', models.DO_NOTHING, db_column='tbl_Disease_sysmptom_idtbl_Disease_sysmptom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_disease_sysmptom'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_disease_sysmptom_idtbl_disease_sysmptom'),)


class TblCattleDeseaseHasTblDrug(models.Model):
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease', primary_key=True)  # Field name made lowercase.
    tbl_drug_idtbl_drug = models.ForeignKey('TblDrug', models.DO_NOTHING, db_column='tbl_Drug_idtbl_Drug')  # Field name made lowercase.
    duration_days_field = models.IntegerField(db_column='Duration(Days)')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_desease_has_tbl_drug'
        unique_together = (('tbl_cattle_desease_idtbl_cattle_desease', 'tbl_drug_idtbl_drug'),)


class TblCattleGender(models.Model):
    idtbl_cattle_gender = models.AutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cattle_gender'


class TblCause(models.Model):
    idtbl_cause = models.AutoField(primary_key=True)
    desciption = models.CharField(db_column='Desciption', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cause'


class TblDetection(models.Model):
    idtbl_detection = models.AutoField(db_column='idtbl_Detection', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    extent = models.CharField(db_column='Extent', max_length=45)  # Field name made lowercase.
    affected_prdediction = models.IntegerField(db_column='Affected_prdediction')  # Field name made lowercase.
    solved = models.IntegerField(db_column='Solved', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_detection'


class TblDetectionHasTblCattle(models.Model):
    tbl_detection_idtbl_detection = models.ForeignKey(TblDetection, models.DO_NOTHING, db_column='tbl_Detection_idtbl_Detection', primary_key=True)  # Field name made lowercase.
    tbl_cattle_idtbl_cattle = models.ForeignKey(TblCattle, models.DO_NOTHING, db_column='tbl_Cattle_idtbl_Cattle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_detection_has_tbl_cattle'
        unique_together = (('tbl_detection_idtbl_detection', 'tbl_cattle_idtbl_cattle'),)


class TblDiseaseSysmptom(models.Model):
    idtbl_disease_sysmptom = models.AutoField(db_column='idtbl_Disease_sysmptom', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_disease_sysmptom'


class TblDrug(models.Model):
    idtbl_drug = models.AutoField(db_column='idtbl_Drug', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_drug'


class TblFarm(models.Model):
    idtbl_farm = models.AutoField(db_column='idtbl_Farm', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=45)  # Field name made lowercase.
    tbl_farming_region_idtbl_farming_region = models.ForeignKey('TblFarmingRegion', models.DO_NOTHING, db_column='tbl_Farming_region_idtbl_Farming_region')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_farm'


class TblFarmingRegion(models.Model):
    idtbl_farming_region = models.AutoField(db_column='idtbl_Farming_region', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    temperature_min = models.FloatField(db_column='Temperature_min')  # Field name made lowercase.
    temperature_max = models.FloatField(db_column='Temperature_max')  # Field name made lowercase.
    rainfall_min = models.FloatField(db_column='Rainfall_min')  # Field name made lowercase.
    rainfall_max = models.FloatField(db_column='Rainfall_max')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_farming_region'


class TblFarmingRegionHasTblCattleDesease(models.Model):
    tbl_farming_region_idtbl_farming_region = models.ForeignKey(TblFarmingRegion, models.DO_NOTHING, db_column='tbl_Farming_region_idtbl_Farming_region', primary_key=True)  # Field name made lowercase.
    tbl_cattle_desease_idtbl_cattle_desease = models.ForeignKey(TblCattleDesease, models.DO_NOTHING, db_column='tbl_Cattle_Desease_idtbl_Cattle_Desease')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_farming_region_has_tbl_cattle_desease'
        unique_together = (('tbl_farming_region_idtbl_farming_region', 'tbl_cattle_desease_idtbl_cattle_desease'),)


class TblGender(models.Model):
    idtbl_gender = models.AutoField(db_column='idtbl_Gender', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gender'


class TblHeard(models.Model):
    idtbl_heard = models.AutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_heard'


class TblLogin(models.Model):
    idtbl_login = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', unique=True, max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_login'


class TblNormalSign(models.Model):
    idtbl_normal_sign = models.AutoField(db_column='idtbl_Normal_Sign', primary_key=True)  # Field name made lowercase.
    feed_min = models.FloatField(db_column='Feed_min')  # Field name made lowercase.
    feed_max = models.FloatField(db_column='Feed_max')  # Field name made lowercase.
    water_min = models.FloatField(db_column='Water_min')  # Field name made lowercase.
    water_max = models.FloatField(db_column='Water_max')  # Field name made lowercase.
    temparature_min = models.FloatField(db_column='Temparature_min')  # Field name made lowercase.
    temperature_max = models.FloatField(db_column='Temperature_max')  # Field name made lowercase.
    respiration_min = models.FloatField(db_column='Respiration_min')  # Field name made lowercase.
    respiration_max = models.FloatField(db_column='Respiration_max')  # Field name made lowercase.
    pulse_max = models.IntegerField(db_column='Pulse_max')  # Field name made lowercase.
    pulse_min = models.IntegerField(db_column='Pulse_min')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_normal_sign'


class TblNotifications(models.Model):
    idtbl_notifications = models.AutoField(db_column='idtbl_Notifications', primary_key=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=45)  # Field name made lowercase.
    submission_date = models.CharField(db_column='Submission_date', max_length=45)  # Field name made lowercase.
    tbl_user_level_idtbl_user_level = models.ForeignKey('TblUserLevel', models.DO_NOTHING, db_column='tbl_User_level_idtbl_User_level')  # Field name made lowercase.
    read = models.IntegerField(db_column='Read')  # Field name made lowercase.
    broadcasted = models.IntegerField(db_column='Broadcasted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_notifications'


class TblReadings(models.Model):
    idtbl_readings = models.AutoField(primary_key=True)
    tempareture = models.CharField(max_length=45)
    tbl_cattle_idtbl_cattle = models.ForeignKey(TblCattle, models.DO_NOTHING, db_column='tbl_Cattle_idtbl_Cattle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_readings'


class TblSeason(models.Model):
    idtbl_season = models.AutoField(db_column='idtbl_Season', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.
    starting_month = models.CharField(db_column='Starting_month', max_length=45)  # Field name made lowercase.
    ending_month = models.CharField(db_column='Ending_month', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_season'


class TblStatus(models.Model):
    idtbl_status = models.AutoField(db_column='idtbl_Status', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_status'


class TblUser(models.Model):
    idtbl_user = models.AutoField(db_column='idtbl_User', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=100)  # Field name made lowercase.
    other_name = models.CharField(db_column='Other_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=100)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='Date_of_birth')  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_address', max_length=200)  # Field name made lowercase.
    mobile_number = models.CharField(db_column='Mobile_number', max_length=45)  # Field name made lowercase.
    tbl_gender_idtbl_gender = models.ForeignKey(TblGender, models.DO_NOTHING, db_column='tbl_Gender_idtbl_Gender')  # Field name made lowercase.
    tbl_farm_idtbl_farm = models.ForeignKey(TblFarm, models.DO_NOTHING, db_column='tbl_Farm_idtbl_Farm')  # Field name made lowercase.
    tbl_user_level_idtbl_user_level = models.ForeignKey('TblUserLevel', models.DO_NOTHING, db_column='tbl_User_level_idtbl_User_level')  # Field name made lowercase.
    tbl_login_idtbl_login = models.ForeignKey(TblLogin, models.DO_NOTHING, db_column='tbl_login_idtbl_login')

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblUserLevel(models.Model):
    idtbl_user_level = models.AutoField(db_column='idtbl_User_level', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_user_level'
