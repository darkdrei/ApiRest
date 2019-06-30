from django import forms

from . import models


class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None or image is None:
            raise forms.ValidationError('Content or image is required.')
        return super(StatusForm, self).clean(*args, **kwargs)
        return content

    def clean_content(self):
        conten = self.cleaned_data.get('content')
        if len(conten) > 240:
            raise forms.ValidationError("Content is too long.")