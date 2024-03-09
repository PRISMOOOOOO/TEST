from django.shortcuts import render
from django.http import HttpResponse

def display_text(request):
    text_to_display = "سلام! این یک مثال ساده از یک برنامه Django است."
    return HttpResponse(text_to_display)