from django.db import models
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel


class Region(BaseModel):

    name = models.CharField(
        verbose_name=_("Region Name"),
        max_length=2048,
        null=False,
        blank=True,
        default="",
        db_index=True,
    )
    population = models.PositiveIntegerField(
        verbose_name=_("Population"), null=True, blank=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return f"Region {self.name}" if self.name else f"Unnamed Region ({self.id})"
