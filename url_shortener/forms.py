from django.forms import ModelForm

from shortener_app.models import AliasedUrl


class AliasedUrlForm(ModelForm):
   class Meta:
        model = AliasedUrl
        fields = ['url']