from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Training
from .serializers import TrainingSerializer

class TrainingList(APIView):
    def get(self, request):
        trainings = Training.objects.all()
        serializer = TrainingSerializer(trainings, many=True)
        return Response(serializer.data)

class TrainingDetail(APIView):
    def get(self, request, pk):
        training = Training.objects.get(pk=pk)
        serializer = TrainingSerializer(training)
        return Response(serializer.data)
