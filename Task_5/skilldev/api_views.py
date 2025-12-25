from rest_framework.response import Response
from rest_framework.decorators import api_view
from skilldev.models import Developer

@api_view(["GET"])
def developer_api(request):
    data = list(Developer.objects.values("id", "name", "age"))
    return Response(data)
