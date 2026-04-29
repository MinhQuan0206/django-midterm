import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Simulate GET request
from django.test import Client

client = Client()
response = client.get('/api/notes/')

print(f"Status Code: {response.status_code}")
print(f"Response:")
data = response.json()
print(json.dumps(data, indent=2, ensure_ascii=False))
