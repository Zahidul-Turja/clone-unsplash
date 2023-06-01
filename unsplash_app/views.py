from django.shortcuts import render
import requests

from .static_data import test_data


# ? Hide before uploading to GitHub
CLIENT_ID = "xJt3ueEHF-iFVzywR-czMBWaDH9O_uvsptbC-kPTQD0"


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

def index(request):
    if request.method == "POST":
        data = api_call(search_key=request.POST.get("search_text"))
    # data = api_call(search_key="cats")
    else:
        data = api_call()
    # data = test_data
    res = {
        "images": data,
    }

    return render(request, "unsplash_app/index.html", res)
