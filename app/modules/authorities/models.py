from django.db import models
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel
from modules.regions.models import Region


class LocalGovernment(BaseModel):

    region = models.ForeignKey(
        to=Region,
        verbose_name=_("Region"),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="local_government",
    )
    official_name = models.CharField(
        verbose_name=_("Official Name"),
        max_length=2048,
        null=False,
        blank=True,
        default="",
        db_index=True,
    )

    class Meta:
        ordering = ("created_at",)
        verbose_name = _("Local Government")
        verbose_name_plural = _("Local Government Units")

    def __str__(self):
        return (
            f"{self.official_name}"
            if self.official_name
            else "Unnamed Local Government Unit"
        )
