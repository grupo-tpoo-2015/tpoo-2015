from django import forms
from django.shortcuts import render


class UploadFileForm(forms.Form):
    file = forms.FileField()


def load(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            print f.read()
    else:
        form = UploadFileForm()

    return render(request, 'usability_tests/load.jinja', {
        'load_data_active': True,
        'form': form,
    })
