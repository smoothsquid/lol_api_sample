from django import views
from django.shortcuts import render

from home.forms import HomeSearchForm


class HomeView(views.View):
    template_name = "index.html"

    def get(self, request):
        context = {
            "search_form": HomeSearchForm(),
        }
        return render(request, self.template_name, context)
