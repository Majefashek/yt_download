from django.shortcuts import render

# Create your views here.
# views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from pytube import YouTube
import requests
from rest_framework.response import Response

@swagger_auto_schema(
    method='post',
    operation_description="Download video from YouTube URL",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'youtube_url': openapi.Schema(type=openapi.TYPE_STRING, description='YouTube URL'),
        }
    ),
    responses={200: 'Video downloaded successfully', 400: 'Error occurred'}
)
@csrf_exempt
@api_view(['POST'])
def download_video(request):
    if request.method == 'POST':
        youtube_url = request.data.get('youtube_url')

        try:
            yt = YouTube(youtube_url)
            stream = yt.streams.get_highest_resolution()
            video_response = requests.get(stream.url, stream=True)
            
            # Ensure the request was successful
            video_response.raise_for_status()
            
            # Get the binary content of the response
            video_data = video_response.content
            
            # Set up HttpResponse with the video data and content type
            response = HttpResponse(video_data, content_type="video/mp4")
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
            return response
        except Exception as e:
            return Response({"Error": f" This is the error {e}"}, status=400)
    return Response({"error":"Method Not Allowed"}, status=405)
