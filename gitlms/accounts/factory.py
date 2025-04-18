from django.utils import timezone
import user_agents
class SessionDisplay:
    def __init__(self, session, request):
        self.session = session
        self.request = request

    def get_display_data(self):
        raise NotImplementedError

class DetailedSessionDisplay(SessionDisplay):
    def get_display_data(self):
        ua_string = self.request.META.get('HTTP_USER_AGENT', '')
        user_agent = user_agents.parse(ua_string)
        return {
            'id': self.session.session_key,
            'device': f"{user_agent.get_device()} {user_agent.get_os()}",
            'location': self._get_ip_location(),
            'last_activity': self.session.expire_date - timezone.timedelta(seconds=3600),
            'current': (self.session.session_key == self.request.session.session_key)
        }

    def _get_ip_location(self):
        ip = self.request.META.get('HTTP_X_FORWARDED_FOR') or self.request.META.get('REMOTE_ADDR')
        return 'Localhost' if ip == '127.0.0.1' else f"IP: {ip.split(',')[0]}"

class SessionDisplayFactory:
    @staticmethod
    def create_display(type, session, request):
        if type == 'detailed':
            return DetailedSessionDisplay(session, request)
        # Add other display types as needed
        raise ValueError(f"Unknown display type: {type}")