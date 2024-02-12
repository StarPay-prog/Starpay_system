from django.shortcuts import render

def index(request):

    context={
        "page_title":"Dashboard"
    }
    
    return render(request,"dashboard/index.html",context)