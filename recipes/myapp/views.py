from django.shortcuts import render

import logging


logger = logging.getLogger(__name__)


def index(request):
    return render(request, "myapp/index.html")
