from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializer import *

# Create your views here.
class ReactView(APIView):
    def get(self, request):
        output = [{"name": output.name,
                   "biography": output.biography}
                   for output in React.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)