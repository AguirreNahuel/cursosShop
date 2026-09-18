import json
import os
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_string(key):
    # Esto busca un nivel más arriba de donde apunta BASE_DIR
    base_dir = os.path.dirname(settings.BASE_DIR)
    file_path = os.path.join(base_dir, 'strings.json')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get(key, f"[{key}]")