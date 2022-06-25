from django.shortcuts import redirect, render
from django.db.models import Avg
from django.core.paginator import Paginator
from django.contrib import messages


from .models import *
def showComments(request):

    # avarageRating = Review.objects.all().aggregate(avarageRating('stars'))

    total_number_of_reviews = Review.objects.all().count()
    raw_reviews = Review.objects.exclude(comment="")
    paginator   = Paginator(raw_reviews,10)
    page_number = request.GET.get('page')
    reviews     = paginator.get_page(page_number)

        

    if total_number_of_reviews>0:
        avarageRating = Review.objects.aggregate(Avg('stars'))

        fiveStars_raw = Review.objects.filter(stars=5).count()
        fiveStars = fiveStars_raw *100/total_number_of_reviews;

        fourStars_raw = Review.objects.filter(stars=4).count()
        fourStars = fourStars_raw *100/total_number_of_reviews;

        threeStars_raw = Review.objects.filter(stars=3).count()
        threeStars = threeStars_raw *100/total_number_of_reviews;

        twoStars_raw = Review.objects.filter(stars=2).count()
        twoStars = twoStars_raw *100/total_number_of_reviews;

        oneStars_raw = Review.objects.filter(stars=1).count()
        oneStars = oneStars_raw *100/total_number_of_reviews;
    else:    
        avarageRating = 0;
        fiveStars = 0;
        fourStars = 0;
        threeStars = 0;
        twoStars = 0;
        oneStars = 0;

        

    # messages.success(request, 'Review submitted - Thank you!')
    # messages.success(request, 'We are processing your review. This might take several days, so we appreciate your patience. We will email you when this is complete.')
    context = {
        'fiveStars':fiveStars,
        'fourStars':fourStars,
        'threeStars':threeStars,
        'twoStars':twoStars,
        'oneStars':oneStars,
        'total':total_number_of_reviews,

    }
    return render(request, 'reviews.html', {'rating':avarageRating, 'reviews':reviews,'context':context })



def WriteReview(request):
    if request.method == "POST":
        starvalue = request.POST.get('startValue')
        commentvalue = request.POST.get('comment')
        user = User.objects.get(username="petergangmei")
        Review.objects.create(author=user, name="Peter Gangmei", stars=starvalue, comment=commentvalue)
        messages.success(request, 'Review submitted - Thank you!')
        messages.success(request, 'We are processing your review. This might take several days, so we appreciate your patience. We will email you when this is complete.')
        return redirect("home")
    else:
        return render(request,'write_reviews.html')