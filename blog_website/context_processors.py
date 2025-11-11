from django.conf import settings

def site_settings(request):
    return {
        'BASE_URL': getattr(settings, 'BASE_URL', ''),
        'SITE_URL': getattr(settings, 'SITE_URL', ''),
    }
