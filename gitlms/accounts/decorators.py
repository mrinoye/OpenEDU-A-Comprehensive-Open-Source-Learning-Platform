# decorators.py
def log_activity(func):
    def wrapper(request, *args, **kwargs):
        print(f"User activity logged for {request.user.username} performing {func.__name__}")
        return func(request, *args, **kwargs)
    return wrapper
