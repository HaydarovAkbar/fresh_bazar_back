import re
from django.http import HttpResponse


class SqlInectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if re.search(r'(?:--|select|insert|update|delete|union|into|load_file|outfile)\b', request.path):
            return HttpResponse("Sql Injection Detected")
        response = self.get_response(request)
        return response
