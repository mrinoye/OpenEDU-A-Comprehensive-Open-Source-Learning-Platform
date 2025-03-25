# gitlms/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from notifications.routing import websocket_urlpatterns  # Import WebSocket routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gitlms.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # For HTTP requests
    "websocket": AuthMiddlewareStack(  # For WebSocket requests
        URLRouter(
            websocket_urlpatterns  # Include WebSocket URL routing here
        )
    ),
})
