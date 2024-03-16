from django.shortcuts import render, get_object_or_404
from .models import Trail, Review, MagicPage

def trail_list(request):
    trails = Trail.objects.all()
    return render(request, 'pages/trail_list.html', {'trails': trails})

def trail_detail(request, trail_id):
    trail = get_object_or_404(Trail, id=trail_id)
    reviews = Review.objects.filter(trail=trail)
    if reviews.exists():
        average_rating = sum(review.rating for review in reviews) / len(reviews)
    else:
        average_rating = None
    return render(request, 'pages/trail_detail.html', {'trail': trail, 'average_rating': average_rating})

def about_page(request):
    return render(request, 'pages/about.html')

def contact_page(request):
    return render(request, 'pages/contact.html')

def admin_page(request):
    return render(request, 'admin.py')


def magic_page(request):
    magic_page = MagicPage.objects.first()  
    return render(request, 'pages/magic_page.html', {'magic_page': magic_page})