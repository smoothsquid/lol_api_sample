from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Champion


@register(Champion)
class ChampionADmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "version",
                    "name_kr",
                    "name_en",
                    "title",
                    "blurb",
                ),
            },
        ),
        (
            "Sprite",
            {
                "fields": (
                    "image_full",
                    "image_group",
                    "image_sprite",
                    "image_sprite_x",
                    "image_sprite_y",
                    "image_sprite_w",
                    "image_sprite_h",
                ),
            },
        ),
    )
    list_display = (
        "id",
        "name_kr",
        "name_en",
        "title",
    )
