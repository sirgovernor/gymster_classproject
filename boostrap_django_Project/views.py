from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def classes(request):
    return render(request, 'class.html')
def contact(request):
    return render(request, 'contact.html')
def detail(request):
    return render(request, 'detail.html')
def team(request):
    return render(request, 'team.html')
def testimony(request):
    return render(request, 'testimonial.html')
