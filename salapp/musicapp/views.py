from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import music
from .serializers import musicSerializer


# Create your views here.
class musicList(APIView):

    def get(self, request):
        music_list = music.objects.all()
        serializer = musicSerializer(music_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


