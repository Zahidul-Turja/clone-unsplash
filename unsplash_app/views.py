from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse

# ! Views
from django.views import View
from django.views.generic import ListView

import requests
from json import dumps

from .forms import UserForm
from .models import User, Post, Tag

from .static_data import test_data, CLIENT_ID

# ? Hide CLIENT_ID before uploading to GitHub

#! functions


def trim_list(list_item: list, page_no: int = 0):
    last_ind = page_no + 9
    return list_item[page_no:last_ind]


def make_url(is_searching: bool, search_key: str = "", page_no=0):
    # ! setting base url
    BASE_URL = "https://api.unsplash.com/"

    if is_searching:
        BASE_URL = BASE_URL + "search/"

    BASE_URL = BASE_URL + "photos?"

    # ! setting url queries
    BASE_URL = BASE_URL + "page=" + str(page_no)

    if is_searching:
        if " " in search_key:
            search_key = search_key.replace(" ", "%20")
        BASE_URL = BASE_URL + "&query=" + search_key

    return BASE_URL + ";client_id=" + CLIENT_ID


def api_call(search_key: str = "", page_no=1):
    """Calls Unsplash Api and returns a list of 10 images detail.

    Args:
        search_key (str, default=""): The search key if is_searching True.
        page (int, default=1): Current Page number.
    """

    is_searching = False

    if search_key:
        is_searching = True

    final_url = make_url(is_searching, search_key, page_no)

    # ? IMPORTANT: search returns dict and normal feed returns list
    response = requests.get(final_url)

    if is_searching and len(response.json()["results"]) > 9*page_no:
        return trim_list(response.json()["results"], page_no)
    elif is_searching:
        return response.json()["results"]

    if len(response.json()) > 9*page_no:
        return trim_list(response.json())
    else:
        return response.json()


#! Create your views here.

def index(request, logged_in=False):
    if request.method == "POST":
        data = api_call(search_key=request.POST.get("search_text"))
    # data = api_call(search_key="cats")
    else:
        data = api_call()
    # data = test_data
    json_data = dumps(data)
    res = {
        "images": data,
        "logged_in": logged_in,
        "json_img": json_data
    }

    return render(request, "unsplash_app/index.html", res)


def login(request):
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_pass = request.POST["login-password"]
        potential_user = User.objects.get(pk=user_name)
        pass_word = potential_user.password
        if potential_user and pass_word == user_pass:
            return HttpResponseRedirect(reverse("logged-in-succ", args=[user_name]))
            # return render(request, "unsplash_app/index.html", {
            #     "test": potential_user,
            # })
        else:
            return render(request, "unsplash_app/test.html", {
                "test": potential_user
            })

    return render(request, "unsplash_app/login.html")


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/login")
        else:
            return render(request, "unsplash_app/test.html", {
                "form": form
            })

    else:
        form = UserForm()

    return render(request, "unsplash_app/signup.html")


def logged_in(request, user_name):
    if request.method == "POST":
        data = api_call(search_key=request.POST.get("search_text"))
    # data = api_call(search_key="cats")
    else:
        data = api_call()
    # data = test_data
    json_data = dumps(data)
    res = {
        "images": data,
        "logged_in": True,
        "json_img": json_data,
        "user_name": user_name
    }

    return render(request, "unsplash_app/index.html", res)


class UserProfile(View):
    template_name = "unsplash_app/profile.html"
    model = User

    def get(self, request, user_name):
        user_info = User.objects.get(pk=user_name)

        context = {
            "name": user_info.name,
            "user_name": user_info.user_name,
            "profile_image": user_info.profile_image,
            "about": user_info.about,
            "posts": user_info.posts.all(),  # type: ignore
            "logged_in": True
        }
        return render(request, "unsplash_app/profile.html", context)
