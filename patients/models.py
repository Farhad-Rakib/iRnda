from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    from_age = models.IntegerField()
    to_age = models.IntegerField()
    question_number = models.IntegerField()
    domain_name  = models.CharField(max_length=155)

    def __str__(self):
        return f"Question {self.question_number}"


class QuestionOption(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.TextField()

    def __str__(self):
        return self.option_text
    
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    birth_weight = models.FloatField()
    sex = models.CharField(max_length=1)  # 'M' for Male, 'F' for Female, etc.

    def __str__(self):
        return self.name

class PatientDetail(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='details', on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_education = models.CharField(max_length=255)
    father_education = models.CharField(max_length=255)
    living_area = models.CharField(max_length=255)
    father_profession = models.CharField(max_length=255)
    mother_profession = models.CharField(max_length=255)
    father_monthly_income = models.FloatField()
    number_of_siblings = models.IntegerField(null= True)

    def __str__(self):
        return f"Details for {self.patient.name}"

class RndaResult(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
    last_date_of_assessment = models.DateField()
    assessment_number = models.IntegerField()
    rnda_score = models.DecimalField(max_digits=10, decimal_places=2)
    rnda_score_text = models.CharField(max_length=155)
    rnda_domain = models.CharField(max_length=255)
    remarks = models.TextField()

