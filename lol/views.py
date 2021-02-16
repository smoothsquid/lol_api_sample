from django import views
from django.shortcuts import render

from .utils import search_match


class SearchMatchView(views.View):
    template_name = "lol/search_result.html"

    def get(self, request):
        query = request.GET.get("query", "")
        context = {
            "id_list": search_match(query),
        }
        return render(request, self.template_name, context)
