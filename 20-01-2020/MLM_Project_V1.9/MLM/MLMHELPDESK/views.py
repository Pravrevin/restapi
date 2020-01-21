from . serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MLMAPP.models import MyUser
from django.http import Http404
from . models import MmlTicket


class TicketList(APIView):

    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def post(self, request,pk, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            x = serializer.data

            InputData = MmlTicket.objects.create(Issue=x['Issue'],Description=x['Description'],number_id=pk)
            InputData.save()
            OutputData = {'Ticket_ID': InputData.ticket_id,'Issue':InputData.Issue,'Description':InputData.Description,
                          'RequestedDate':InputData.RequestedDate,'status':InputData.status,'number':InputData.number_id}
            return Response(OutputData, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
