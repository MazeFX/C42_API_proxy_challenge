from django.conf.urls import url

from .api_requests import get_events_with_subscriptions


urlpatterns = [
    # URL pattern for events with subscriptions
    url(r'^events-with-subscriptions/$', get_events_with_subscriptions, name='events-with-subscriptions'),
]
