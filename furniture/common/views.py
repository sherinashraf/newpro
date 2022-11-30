from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_sofa(request):
    return render(request,'common_templates/sofa.html')

def common_beds(request):
    return render(request,'common_templates/beds.html')

def common_storage(request):
    return render(request,'common_templates/storage.html')

def common_dining(request):
    return render(request,'common_templates/dining.html')