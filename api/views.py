from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def APIOverview(request):
    user = { 'name': 'João', 'age': 22 }
    return Response(user)
