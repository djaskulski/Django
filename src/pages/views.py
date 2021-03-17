# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def mindfulness_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "mindfulness.html", {})


def minimalism_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "minimalism.html", {})


def recycling_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "recycling.html", {})


def vegetarianism_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "vegetarianism.html", {})


def yoga_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "yoga.html", {})


def contact_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "my_number": "661389770",
        "True_statement": True,
        "my_html": "<h1>www.healyourbeing.com</h1>",
        "my_list": ["Ola", "Kasia", "Madzia", "Zosia", "Stasia", "Joasia", "Michasia"]
    }
    # return HttpResponse("<h1>Hello About</h1>")
    return render(request, "about.html", my_context)
