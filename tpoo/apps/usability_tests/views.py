from django import forms
from django.shortcuts import render
from .models import SqlDump


class SqlDumpForm(forms.ModelForm):

    class Meta:
        model = SqlDump
        fields = ('name', 'script_file')

    def save(self, user, *args, **kwargs):
        self.instance.uploaded_by = user
        super(SqlDumpForm, self).save(*args, **kwargs)


def load(request):

    if request.method == 'POST':
        form = SqlDumpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
    else:
        form = SqlDumpForm()

    return render(request, 'usability_tests/load.jinja', {
        'load_data_active': True,
        'form': form,
        'dumps': SqlDump.objects.all(),
    })
