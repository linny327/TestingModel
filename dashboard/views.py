from django.shortcuts import render
import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import  *

notification_count = 0

# Create your views here.
def dashboard(request):
    try:
        user_details = TblUser.objects.all()
        notification_count = TblNotifications.objects.filter(read=0).count()
        cattle_count = TblCattle.objects.filter(tbl_status_idtbl_status__description__exact='HEALTHY').count() + \
                       TblCattle.objects.filter(tbl_status_idtbl_status__description__exact='SICK').count()
        registered_farms = TblFarm.objects.all().count()
    except TblUser.DoesNotExist:
        return Http404("No users registered in the system")
    return render(request, "dashboard.html", {'user_details': user_details[:4],
                                              'notifications': notification_count,
                                              'cattle_count': cattle_count,
                                              'registered_farms': registered_farms})


def add_cattle(request):
    herds = TblHeard.objects.all()
    cattle_gender = TblCattleGender.objects.all()
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "add_cattle.html", {'herds': herds,
                                               'cattle_gender': cattle_gender})


def add_user(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "add_user.html")


def cattle(request):
    notification_count = TblNotifications.objects.filter(read=0).count()

    cattle_details = TblCattle.objects.all()
    return render(request, "cattle.html", {'cattle_details': cattle_details})


def chart(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "chart.html")


def disease(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "disease.html")


def farm(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "farm.html")


def monitor(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "monitor.html")


def notification(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "notifications.html")


def predict_diagnose(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "predict_diagnose.html")


def profile(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    return render(request, "profile.html")


def user(request):
    notification_count = TblNotifications.objects.filter(read=0).count()
    try:
        user_details = TblUser.objects.select_related('tbl_login_idtbl_login')
        print(str(user_details.query))
    except TblUser.DoesNotExist:
        return Http404("No users registered in the system")
    return render(request, "user.html", {'user_details': user_details,
                                         'notification_count': notification_count})


def view_cattle(request, id):
    notification_count = TblNotifications.objects.filter(read=0).count()

    cattle_details = TblCattle.objects.filter(idtbl_cattle=id)

    return render(request, "view_cattle.html", {'notification_count': notification_count,
                                                'cattle_details': cattle_details})


def view_user(request, id):
    notification_count = TblNotifications.objects.filter(read=0).count()

    user_details = TblUser.objects.filter(idtbl_user=id)

    return render(request, "view_user.html", {'notification_count': notification_count,
                                              'user_details': user_details})


def new_user(request):
    if request.method == 'POST':
        TblLogin.objects.create(
            username=request.POST['username'],
            password=request.POST['password']
        )
        # IntegrityError

        login_id = TblLogin.objects.values_list('idtbl_login').filter(username=request.POST['username'])
        year = request.POST['year']
        month = request.POST['month']
        day = request.POST['day']
        fullday = year + month + day
        TblUser.objects.create(
            first_name=request.POST['first_name'],
            other_name=request.POST['surname'],
            surname=request.POST['other_name'],
            date_of_birth=datetime.datetime.strptime(fullday,
                                                     "%y%m%d%").date(),
            email_address=request.POST['e_mail'],
            mobile_number=request.POST['mobile_number'],
            tbl_gender_idtbl_gender=1 if request.POST['gender'] == 'MALE' else 2,
            tbl_farm_idtbl_farm_id=1,
            tbl_user_level_idtbl_user_level=1,
            tbl_login_idtbl_login=login_id
        )

        # login_id = TblLogin.objects.values_list('idtbl_login').filter(username=request.POST['username'])
        #
        # first_name = request.POST['first_name']
        # other_name = request.POST['other_name']
        # surname = request.POST['surname']
        # year = request.POST['year']
        # month = request.POST['month']
        # day = request.POST['day']
        # fullday = year + month + day
        #
        #
        # email_address = request.POST['e_mail']
        # mobile_number = request.POST['mobile_number']
        # tbl_gender_idtbl_gender = 1 if request.POST['gender'] == 'MALE' else 2
        # username = request.POST['username']
        # password = request.POST['password']
        # tbl_farm_idtbl_farm_id = 1
        # tbl_user_level_idtbl_user_level = 1
        # tbl_login_idtbl_login = 0

    return HttpResponse()


def new_farm(request):
    return render(request, "farm.html")


def edit_user(request):
    return render(request, "edit_user.html")


def edit_cattle(request):
    return render(request, "edit_cattle.html")


def graph(request):
    return render(request, "graph.html")

