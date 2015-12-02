from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .forms import SqlDumpForm
from .models import SqlDump
from tpoo.utils.views import LoginRequiredMixin


class LoadView(LoginRequiredMixin, View):

    template_name = 'usability_tests/load.jinja'

    def _render(self, request, form):
        return render(request, self.template_name, {
            'load_data_active': True,
            'form': form,
            'dumps': SqlDump.objects.all(),
        })

    def get(self, request):
        form = SqlDumpForm()
        return self._render(request, form)

    def post(self, request):
        form = SqlDumpForm(request.POST, request.FILES)
        if form.is_valid():
            dump = form.save(request.user)
            if SqlDump.objects.count() == 1:
                dump.choose()
        return self._render(request, form)


class DeleteDumpView(LoginRequiredMixin, View):

    def post(self, request, dump_id):
        dump = get_object_or_404(SqlDump, id=dump_id)
        dump.delete()
        return redirect('load')


class ChooseDumpView(LoginRequiredMixin, View):

    def post(self, request, dump_id):
        dump = get_object_or_404(SqlDump, id=dump_id)
        if dump.is_the_current_one:
            raise Exception("El dump no puede ser borrado porque es el actual")
        dump.choose()
        return redirect('load')
