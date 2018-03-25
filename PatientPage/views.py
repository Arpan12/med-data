from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Details
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .form import ChangeProfilePic

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.

def index(request,Patient_name):
     all_patient = Details.objects.all()

     template = loader.get_template('PatientPage/patient.html')
     context = {
       'all_patient' : all_patient,
     }
     return HttpResponse(template.render(context,request))


def changeProfilePic(request,Patient_name):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html')

        form = ChangeProfilePic(request.POST or None, request.FILES or None)
        if form.is_valid():
            Details = form.save(commit=False)
            Details.Name = Patient_name
            Details.profilePic = request.FILES['profilePic']
            file_type = Details.profilePic.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'Details': Details,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'PatientPage/ChangeProfilePic.html', context)

                Details.save()
            return render(request, 'PatientPage/patient.html',{'Details': Details})
        context = {
            "form": form,
        }
        return render(request, 'PatientPage/ChangeProfilePic.html', context)







