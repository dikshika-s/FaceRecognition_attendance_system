from django.shortcuts import render
from django.http import JsonResponse
import csv
from .main import run_script
import os

basepath = os.path.abspath(os.path.dirname(__file__))

# Create your views here.

def home(request):
	return render(request, "main/home.html", {})

def register_form(request):
	return render(request, 'main/r_form.html')

def upload(request):
    print(request.FILES, type(request.FILES))	
    img = request.FILES.get('upload')
    a= os.path.splitext(img.name)[0]
    img_extension = os.path.splitext(img.name)[1]

    user_folder = 'st_images'
    #to upload files to st_images
    img_save_path = os.path.join(basepath, "%s/%s%s"  % (user_folder, a, img_extension))
    with open(img_save_path, 'wb') as f:
        for chunk in img.chunks():
            f.write(chunk)
    return render(request, 'main/home.html', {'done':True})
    
def run_graph(main):
    a = run_script()
    if(a==0):
        return JsonResponse({'already':1})
    return JsonResponse({'already':0})

def view(request):
	with open(os.path.join(basepath,'attendance1.csv'), 'r') as f:
		reader = list(csv.reader(f))
	return render(request, 'main/view.html', {'data' : reader[1:], 'headers' : reader[0]})