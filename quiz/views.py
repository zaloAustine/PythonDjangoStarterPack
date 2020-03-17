from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        message = "this is a get url"
        return Response(data=message ,status = status.HTTP_200_OK)
    elif request.method =='POST':
        message = "this is a post url"
        return Response(data=message ,status = status.HTTP_200_OK)
    else:
        message = "this is a Error"
        return Response(data=message ,status = status.HTTP_200_OK)


class Messsage(APIView):
    def get(self,request):
        return Response(data="Class based view get",status=status.HTTP_200_OK)

    def post(self,request):
        return Response(data="Class based view post",status=status.HTTP_200_OK)



   
     


