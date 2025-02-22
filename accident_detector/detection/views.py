from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Accident

class AccidentAlert(APIView):
    def post(self, request):
        location = request.data.get('location')
        severity = request.data.get('severity')
        description = request.data.get('description')
        video_feed = request.data.get('video_feed')  # Optional video feed URL

        # Save the accident data
        accident = Accident.objects.create(location=location, severity=severity, description=description, video_feed=video_feed)
        return Response({"message": "Accident alert received"}, status=status.HTTP_201_CREATED)

