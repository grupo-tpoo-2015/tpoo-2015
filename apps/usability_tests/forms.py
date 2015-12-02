from django import forms
from .models import SqlDump


class SqlDumpForm(forms.ModelForm):

    class Meta:
        model = SqlDump
        fields = ('name', 'script_file')

    def save(self, user, *args, **kwargs):
        self.instance.uploaded_by = user
        return super(SqlDumpForm, self).save(*args, **kwargs)
