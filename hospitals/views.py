from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date

from django.views.generic import ListView, CreateView, DetailView
from hospitals.libs import custom_forms
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def About(request):
    return render(request,'about.html')

def Index(request):
    return render(request,'index.html')

def contact(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.objects.create(name=n, contact=c, email=e, subject=s, message=m, msgdate=date.today(), isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def adminlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login.html', locals())

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    dc = Doctor.objects.all().count()
    nc = Nurse.objects.all().count()
    pc = Patient.objects.all().count()
    ac = Appointment.objects.all().count()
    of = ClinicalOfficer.objects.all().count()

    d = {'dc': dc, 'nc': nc, 'pc': pc, 'ac': ac, 'of': of}
    return render(request,'admin_home.html', d)

def nurse_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request,'login_nurse.html', locals())


# def nurse_home(request):
#     if not request.user.is_staff:
#         return redirect('login_nurse')
#     pc = Patient.objects.all().count()
#     ac = Appointment.objects.all().count()

#     d = {'pc':pc, 'ac':ac}
#     return render(request, 'nurse_home.html', d)  



def Logout(request):
    logout(request)
    return redirect('index')

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
    return render(request,'add_doctor.html', locals())

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor.html')

def edit_doctor(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        doctor.name = n1
        doctor.mobile = m1
        doctor.special = s1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', locals())

def add_clinical_officer(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            ClinicalOfficer.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
    return render(request,'add_clinical_officer.html', locals())

def view_clinical_officer(request):
    if not request.user.is_staff:
        return redirect('login')
    off = ClinicalOfficer.objects.all()
    d = {'off':off}
    return render(request,'view_clinical_officer.html', d)

def Delete_Clinical_Officer(request,officer_id):
    if not request.user.is_staff:
        return redirect('login')
    officer = ClinicalOfficer.objects.get(id=officer_id)
    officer.delete()
    return redirect('view_clinical_officer.html')

def edit_clinical_officer(request,officer_id):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    officer = ClinicalOfficer.objects.get(id=officer_id)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        officer.name = n1
        officer.mobile = m1
        officer.special = s1

        try:
            officer.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_clinical_officer.html', locals())

def add_nurse(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Nurse.objects.create(name=n,mobile=m,special=sp)
            error="no"
        except:
            error="yes"
    return render(request,'add_nurse.html', locals())

def view_nurse(request):
    if not request.user.is_staff:
        return redirect('login')
    nur = Nurse.objects.all()
    d = {'nur':nur}
    return render(request,'view_nurse.html', d)

def edit_nurse(request,nurse_id):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    nurse = Nurse.objects.get(id=nurse_id)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        s1 = request.POST['special']

        nurse.name = n1
        nurse.mobile = m1
        nurse.special = s1

        try:
            nurse.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_nurse.html', locals())

def Delete_Nurse(request,nurse_id):
    if not request.user.is_staff:
        return redirect('login')
    nurse = Nurse.objects.get(id=nurse_id)
    nurse.delete()
    return redirect('view_nurse.html')

 

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "yes"
    return render(request,'add_patient.html', locals())

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient.html')

def edit_patient(request,pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    patient = Patient.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        m1 = request.POST['mobile']
        g1 = request.POST['gender']
        a1 = request.POST['address']

        patient.name = n1
        patient.mobile = m1
        patient.gender = g1
        patient.address = a1
        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())



def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    d = {'appointment':appointment}
    return render(request,'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment1 = Appointment.objects.get(id=pid)
    appointment1.delete()
    return redirect('view_appointment.html')

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'view_queries.html', locals())


class NurseView(LoginRequiredMixin, ListView):
    """
    Nurse index page with a list of patients
    """
    
    model = Patient
    login_url = "/login_nurse"
    paginate_by = 10
    template_name = "hospitals/nurse/index.html"
    context_object_name = "patient_list"


class AddNoteView(LoginRequiredMixin, CreateView):
    """
    Add a specific patient note for the doctor to read.
    """
    
    model = Note
    login_url = "/login_nurse"
    template_name = "hospitals/nurse/add_note.html"
    form_class = custom_forms.AddNote
    
    def get(self, request: HttpRequest, patient_id: int) -> HttpResponse:
        """
        Return: Add note page.
        """
        
        form = self.form_class(None)
        return render(request, self.template_name, {
            "form": form
        })
    
    def form_valid(self, form, *args, **kwargs) -> HttpResponse:
        """
        Add Nurse and Patient fields.
        """
        
        try:
            form.instance.nurse = self.request.user
            form.instance.patient_id = self.kwargs["patient_id"]
        except Exception as error:
            print(f"Error : {str(error)}")
        return super(AddNoteView, self).form_valid(form)


class NoteDetails(LoginRequiredMixin, DetailView):
    model = Note
    login_url = "/login_nurse"
    template_name = "hospitals/nurse/notes_details.html"
    context_object_name = "note"
    
    
