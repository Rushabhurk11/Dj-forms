from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.

def studentFormView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # form.save() # Save the form data to the database
            success=True
            form = StudentForm() # Reset the form after saving
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     