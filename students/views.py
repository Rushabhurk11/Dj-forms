from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_view')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'students/student_view.html', {'form': form, 'students': students})
