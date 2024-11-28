from django.shortcuts import render, redirect


def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "index.html")


def vision(request):
    return render(request, "vision.html")


def demolition(request):
    return render(request, "demolition.html")


def sanding(request):
    return render(request, "sanding.html")


def weare(request):
    return render(request, "weare.html")
