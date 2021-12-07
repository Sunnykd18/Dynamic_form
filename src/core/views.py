from django.shortcuts import render

def BootstarpFilterView(request):
    return render(request, "bootstrap_form.html",{})
