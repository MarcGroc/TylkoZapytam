from django.http import HttpResponse
from django.views import View

# from rest_framework.views import APIView


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello")

    def post(self, request):
        return HttpResponse("Hello")

    def put(self, request):
        return HttpResponse("Hello")

    def delete(self, request):
        return HttpResponse("Hello")
