from django.shortcuts import render, redirect, get_object_or_404
from .models import TourPackage, Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect


# Create your views here.

def homepage(request):
    tour_packages = TourPackage.objects.all()
    return render(request, 'TourPackage/homepage.html', {'tour_packages': tour_packages})


def tour_detail(request, tour_id):
    tour_package = get_object_or_404(TourPackage, id=tour_id)
    reviews = Review.objects.filter(tour_package=tour_package)
    return render(request, 'TourPackage/tour_detail.html', {'tour_package': tour_package, 'reviews': reviews})


def review_submission(request, tour_id):
    tour_package = get_object_or_404(TourPackage, id=tour_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour_package = tour_package
            review.save()
            return redirect('tour_detail', tour_id=tour_id)
    else:
        form = ReviewForm(initial={'tour_package': tour_package})
    return render(request, 'TourPackage/review_submission.html', {'form': form})
