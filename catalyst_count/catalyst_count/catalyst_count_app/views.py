#from django.shortcuts import render

# Create your views here.
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import YourModel  # Import your model

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('path/to/save/file.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    process_file('path/to/save/file.csv')

def process_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Process each row and save to database
            YourModel.objects.create(
                field1=row[0],
                field2=row[1],
                # map other fields accordingly
            )

def success(request):
    return HttpResponse('File uploaded and processed successfully.')
