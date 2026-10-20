
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm


# READ: Display all patients
def patient_list(request):
    patients = Patient.objects.all().order_by('-created_at')

    return render(request, 'patients/patient_list.html', {
        'patients': patients
    })


# CREATE: Register a new patient
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'patients/patient_form.html', {
        'form': form,
        'action': 'Register'
    })


# UPDATE: Edit an existing patient
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/patient_form.html', {
        'form': form,
        'action': 'Update'
    })


# DELETE: Remove a patient after confirmation
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'patients/patient_confirm_delete.html', {
        'patient': patient
    })
