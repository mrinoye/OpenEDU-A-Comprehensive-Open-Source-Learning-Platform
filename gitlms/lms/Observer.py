from django.contrib import messages

class Observer:
    def update(self, request, message):
        pass


class EmailObserver(Observer):
    def update(self, request, message):
        # Here, you'd add your email notification logic.
        print(f"Email sent with message: {message}")


class SMSObserver(Observer):
    def update(self, request, message):
        # Here, you'd add your SMS notification logic.
        print(f"SMS sent with message: {message}")


class MessageObserver(Observer):
    def update(self, request, message):
        messages.success(request,message)
        print(f"Message: {message}")


class Subject:
    def __init__(self):
        # Initialize the observers list and attach the default MessageObserver
        self._observers = []
        self.attach(MessageObserver())  # Attach MessageObserver by default

    def attach(self, observer: Observer):
        """Attach an observer to the subject."""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """Remove an observer from the subject."""
        self._observers.remove(observer)

    def notify(self, request, message):
        """Notify all observers about the change."""
        for observer in self._observers:
            observer.update(request, message)
