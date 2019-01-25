from django.urls import reverse_lazy, path
from django.views.generic.base import RedirectView

urlpatterns = [path(r"", RedirectView.as_view(url=reverse_lazy("admin:index")))]
