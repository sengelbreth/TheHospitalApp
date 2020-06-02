from django.shortcuts import render

# Create your views here.
from journals.models import Patient, Doctor, Records

def index(request):
    """View function for home page of site."""

    num_Records = Records.objects.all().count()
    Doctors = Doctor.objects.all()

    context = {
        'num_Records': num_Records,
        'Doctors': Doctors,
        
    }

    return render(request, 'index.html', context=context)