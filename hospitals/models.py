from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name;

class Nurse(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name;

class ClinicalOfficer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name;


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
       return self.name;

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
       return self.doctorname+"--"+self.patient.name;

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id


class Note(models.Model):
    """
    The nurses can keep track of patient recovery progress.
    """
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    note = models.TextField(max_length=10000)
    date_t = models.DateTimeField(auto_now_add=True)
    # Priority to help doctor(s) how/when to respond.
    HIGH = "HIGH"
    NORMAL = "NORM"
    LOW = "LOW"
    PRIORITY_OPTIONS = [
        (HIGH, "High"), (NORMAL, "Normal"), (LOW, "Low")
    ]
    # Assign every note high priority by default.
    priority = models.CharField(max_length=4, choices=PRIORITY_OPTIONS, default=HIGH)
    
    def __str__(self) -> str:
        """Get summary
        Return: Small summary about a given note.
        """
        if len(self.title) > 0:
            return f"{self.title[:70]}{'...' if len(self.title) > 70 else ''}"
        return f"{self.note[:70]}{'...' if len(self.note) > 70 else ''}"
