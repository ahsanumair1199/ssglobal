from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services/services.html')

def warehouse_logistics(request):
    return render(request, 'pages/services/warehouse_logistics.html')
def storage_transport(request):
    return render(request, 'pages/services/storage_transport.html')

def freight_forwarding(request):
    return render(request, 'pages/services/freight_forwarding.html')

def removals_relocations(request):
    return render(request, 'pages/services/removals_relocations.html')

def project_logistics(request):
    return render(request, 'pages/services/project_logistics.html')

def logistics_management(request):
    return render(request, 'pages/services/logistics_management.html')

def road_project(request):
    return render(request, 'pages/projects/road_project.html')

def sea_project(request):
    return render(request, 'pages/projects/sea_project.html')

def railway_project(request):
    return render(request, 'pages/projects/railway_project.html')

def road_transportation(request):
    return render(request, 'pages/transport/road_transportation.html')

def airy_transportation(request):
    return render(request, 'pages/transport/airy_transportation.html')

def sea_transportation(request):
    return render(request, 'pages/transport/sea_transportation.html')

def railway_transportation(request):
    return render(request, 'pages/transport/railway_transportation.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = request.POST['subject']
        email_message = "Name: {}\nEmail: {}\nPhone: {}\nSubject: {}\nMessage: {}".format(name,email,phone,subject,message)
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, recipient_list=['ahsanumair1166@gmail.com'])
    return render(request, 'pages/contact.html')

def global_coverage(request):
    return render(request, 'pages/global_coverage.html')

def get_quote(request):
    return render(request, 'pages/get_quote.html')