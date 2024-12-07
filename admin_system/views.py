from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def show(request):
    return render(request, 'pages/presnt_student.html')
def halls(request):
    return render(request, 'pages/halls.html')
