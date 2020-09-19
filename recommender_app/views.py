from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.


def index(request):
    context = dict()

    if request.method == "POST":
        return redirect(reverse("anime"))

    return render(request, "recommender_app/index.html", context)


def anime(request):
    context = {}
    if request.method == "POST":
        print("Method is POST")
        inp = request.POST.get("anime_field", None)
        if inp:
            from scripts.Anime.anime import anime_recommendation

            # res = anime_recommendation(inp)
            # print(res)

    context = dict()

    return render(request, "recommender_app/anime.html")


def anime_results(request):

    if not request.user.is_authenticated:
        messages.warning(request, "Sorry, you dont have access to that page.")
        return redirect(reverse("index"))
    context = {}
    success = False

    if request.method == "POST":
        print("Anime results view reached, method is post!")

    inp = request.POST.get("anime_field", None)
    if inp:
        from scripts.Anime.anime import anime_recommendation

        print("About to run the anime script")

        try:
            df = anime_recommendation(inp)
            error = False

        except:
            error = True

        print("Script successfully run")
        success = True

    context["success"] = success
    # context['df' : df]

    # return render(request, 'recommender_app/anime_results.html', context)
    # return render(request, df.to_html(), context)
    if not error:
        return HttpResponse(df.to_html())

    else:
        return render(request, "recommender_app/anime_results.html", {"error": error})


def music(request):
    context = dict()

    return render(request, "recommender_app/music.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
        else:
            errors = form.errors
            return render(request, "recommender_app/signup.html", {"form": form})
            print("error!")

    else:
        form = UserCreationForm()
        return render(request, "recommender_app/signup.html", {"form": form})
