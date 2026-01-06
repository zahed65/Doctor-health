from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Article, DoctorInfo, Patient, Appointment
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import F, Q
from .models import Article, Category

def index(request):
    services = Service.objects.all()[:6]
    articles = Article.objects.order_by('-created_at')[:5]
    doctor = DoctorInfo.objects.first()
    ctx = {
        'services': services,
        'articles': articles,
        'doctor': doctor,
    }
    return render(request, 'index.html', ctx)
def about(request):
    doctor = DoctorInfo.objects.first()
    return render(request, 'about.html', {'doctor': doctor})

def contact(request):
    return render(request, 'contact.html')

def article_list(request):
    q = request.GET.get("q", "")
    category = request.GET.get("category")

    articles = Article.objects.all()

    if q:
        articles = articles.filter(
            Q(title__icontains=q) |
            Q(excerpt__icontains=q)
        )

    if category:
        articles = articles.filter(category__id=category)

    paginator = Paginator(articles, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "articles.html", {
        "articles": page_obj,
        "categories": Category.objects.all(),
        "q": q
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    Article.objects.filter(id=article.id).update(views=F("views") + 1)

    return render(request, "list.html", {
        "article": article
    })
