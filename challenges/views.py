from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.shortcuts import render
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes everyday!",
    "march": "Learn Django for 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 30 minutes everyday!",
    "june": "Learn Django for 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes everyday!",
    "september": "Eat no meat for the entire month!",
    "october": "Learn Django for 20 minutes every day!",
    "november": "Walk for at least 20 minutes everyday!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })

    except:
        raise Http404()
