from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PatientForm, PatientDetailForm
from .models import Patient, PatientDetail

# Create your views here.

def index(request):
    return render(request, 'home.html')

def demographic_information(request):
    return render(request, 'demographic_info.html')

def patient_step_1(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()  # Save patient to DB, but do not commit yet
            request.session['patient_id'] = patient.id  # Store patient id in session
            return redirect('patient_step_2')
    else:
        form = PatientForm()

    return render(request, 'patient_step_1.html', {'form': form})

def patient_step_2(request):
    if 'patient_id' not in request.session:
        return redirect('patient_step_1')  # Redirect if patient data not found in session

    patient = Patient.objects.get(id=request.session['patient_id'])
    if request.method == 'POST':
        form = PatientDetailForm(request.POST)
        if form.is_valid():
            patient_detail = form.save(commit=False)  # Don't save yet
            patient_detail.patient = patient  # Assign the patient
            patient_detail.save()  # Now save the patient details
            return redirect('success')  # Redirect to success page after form submission
    else:
        form = PatientDetailForm()

    return render(request, 'patient_step_2.html', {'form': form})

def rnda_results(request):
    # Example results, you could get these from a form or database
    fine_motor_result = 'Normal'  # This can be 'Normal', 'Moderate', or 'Severe'
    gross_motor_result = 'Moderate'
    vision_result = 'Severe'

    return render(request, 'rnda_results.html', {
        'fine_motor_result': fine_motor_result,
        'gross_motor_result': gross_motor_result,
        'vision_result': vision_result,
    })