from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import React
from .serializer import ReactSerializer

class ReactView(APIView):
    def get(self, request):
        output = [{"name": output.name, "biography": output.biography} for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
