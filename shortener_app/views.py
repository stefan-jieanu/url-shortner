from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from shortener_app.models import AliasedUrl
from url_shortener.forms import AliasedUrlForm


def redirect_view(request, alias):
    try:
        aliased_url = AliasedUrl.objects.get(alias=alias)
        return redirect(aliased_url.url)
    except AliasedUrl.DoesNotExist:
        from django.http import Http404
        raise Http404("There is no such alias")


class AliasCreateView(CreateView):
    form_class = AliasedUrlForm
    template_name = 'create_alias.html'
    success_url = reverse_lazy('create')

    def get_success_url(self):
        return f"{reverse_lazy('create')}?created_alias={self.object.alias}"