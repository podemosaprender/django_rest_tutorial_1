#VER: https://www.django-rest-framework.org/api-guide/exceptions/

from rest_framework.views import exception_handler

def debug_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    print(f"DRF exception {exc} {context} {response}")

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response
