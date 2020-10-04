class CsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.validate_csrf_token(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def validate_csrf_token(self, request):
        # validation logic here
        pass
        # if not request.headers.get('Csrf'):
        #     raise PermissionError("CSRF Not Provided")
        # if request.user.is_authenticated and request.headers['Csrf']!=str(request.user.username):
        #     raise PermissionError("CSRF Not validated")
        # else:
        #     return True
