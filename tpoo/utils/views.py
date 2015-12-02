from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# IMPORTANT: this mixin should be put first in the inheritance chain
class LoginRequiredMixin(object):
    u"""Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
