from django.shortcuts import render

def article_page(request):
    return render(request, "article_page.html")