from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from jinja2 import Environment
from .jsonify import jsonify
from usability_tests.models import UsabilityTest


def cool_reverse(name, *args):
    return reverse(name, args=args)


def enumeration(things):
    if not things:
        return ""
    parts = [unicode(thing) for thing in things]
    first_parts, last_part = parts[:-1], parts[-1]
    return " y ".join(x for x in [', '.join(first_parts), last_part] if x)


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': cool_reverse,
        'jsonify': jsonify,
        'usability_tests': UsabilityTest.objects.all,
        'enumeration': enumeration,
    })
    return env
