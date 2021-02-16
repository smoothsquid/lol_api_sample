from django import forms
from django.utils.translation import gettext as _

from config.forms import BaseForm


class HomeSearchForm(BaseForm):

    query = forms.CharField(
        label=_("소환사 이름"),
        max_length=18,
        required=True,
    )
