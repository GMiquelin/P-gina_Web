from django.shortcuts import render

# Create your views here.

def design_co_index(request):
    return render(
        request,
        "index.html"
    )

def design_co_elementos_designer(request):
    return render(
        request,
        "elementos_designer.html"
    )

def design_co_contatos(request):
    return render(
        request,
        "contatos.html"
    )