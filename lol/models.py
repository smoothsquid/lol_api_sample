from django.db import models
from django.utils.translation import gettext as _


class Version(models.Model):
    id = models.CharField(
        _("버전"),
        max_length=10,
        primary_key=True,
    )


class Champion(models.Model):
    id = models.IntegerField(_("ID"), primary_key=True)
    version = models.ForeignKey(
        "lol.Version",
        verbose_name=_("버전"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name_kr = models.CharField(_("이름"), max_length=15)
    name_en = models.CharField(_("Name"), max_length=50)
    blurb = models.TextField(_("이야기"), blank=True)
    image_full = models.CharField(_("아이콘 이미지"), max_length=50)
    image_group = models.CharField(_("이미지 그룹"), max_length=50)
    image_sprite = models.CharField(_("스프라이트 이미지"), max_length=50)
    image_sprite_x = models.SmallIntegerField(_("스프라이트 x"))
    image_sprite_y = models.SmallIntegerField(_("스프라이트 y"))
    image_sprite_w = models.SmallIntegerField(_("스프라이트 w"))
    image_sprite_h = models.SmallIntegerField(_("스프라이트 h"))
