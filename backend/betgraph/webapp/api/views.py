from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import PersonSerializer
from ..models import Person


class IndexAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'status': 'ok',
            'message': 'Welcome to BetGraph API'
        }, status=200)


class PersonDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, username):
        try:
            person = Person.nodes.get(username=username)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response({
                'message': 'Person with a username "{}" does not exist'.format(username)
            }, status=404)


class NewEntryView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PersonSerializer

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = Person.nodes.get_or_none(username=serializer.validated_data['username'])
            return Response({
                'message': request.data
            })
        else:
            return Response({
                'status': 'fail',
                'message': 'Data submitted is invalid. Please try again.'
            })
