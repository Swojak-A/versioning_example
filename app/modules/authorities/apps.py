from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthoritiesConfig(AppConfig):
    name = "modules.authorities"
    verbose_name: str = _("Authorities Module")
