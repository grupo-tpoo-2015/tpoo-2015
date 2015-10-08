import json
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder


def jsonify(data):
    return mark_safe(json.dumps(data, cls=DjangoJSONEncoder))