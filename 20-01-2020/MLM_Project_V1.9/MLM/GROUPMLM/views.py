from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Group , Share
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.http import Http404
from .serializers import  CommentSerializer,GroupSerializer ,ShareSerializer
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
#from django.utils import simplejson


class GroupList(APIView):

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            x = serializer.data

            group = Group.objects.get(state = '1')

            print('state = ',group.state)

            if (group.state == '1'):

                GroupId = group.group_id
                print('group id',GroupId)

                groupCount = Share.objects.filter(group_id_id=GroupId).count()
                print('group_count',groupCount)

                count_share = int(x['NumberOfShares'])

                if((groupCount<100) and  count_share<=(100-(groupCount))):
                    for var in range(count_share):
                        p1 = Share(group_id_id=GroupId, user_id_id=x['UserId'])
                        p1.save()



                elif(groupCount==100):

                    GroupChangeState = Group.objects.get(group_id=GroupId)
                    print('Groupchage state', GroupChangeState.state)
                    GroupChangeState.EffectiveStartDate = datetime.now()
                    GroupChangeState.EffectiveEndDate = GroupChangeState.EffectiveStartDate + relativedelta(months=+10)
                    GroupChangeState.state = '0'
                    GroupChangeState.g_status = '1'

                    GroupChangeState.save()

                    NewGroup = Group(created_date=datetime.now(), EffectiveStartDate=datetime.now(),
                                     EffectiveEndDate=datetime.now(), state='1', g_status='0')
                    NewGroup.save()
                    NewGroup = Group.objects.get(state='1')
                    NewGroupId = NewGroup.group_id
                    for var in range(count_share):
                        p2 = Share(group_id_id=NewGroupId, user_id_id=x['UserId'])
                        p2.save()

                else:
                    remainingshare = 0
                    avialableShare = 100 - groupCount

                    if (groupCount < 100):
                        remainingshare = count_share - avialableShare

                        for var in range(avialableShare):
                            print(var)
                            p = Share(group_id_id=GroupId, user_id_id=x['UserId'])
                            p.save()

                        GroupChangeState = Group.objects.get(group_id=GroupId)
                        GroupChangeState.EffectiveStartDate = datetime.now()
                        GroupChangeState.EffectiveEndDate = GroupChangeState.EffectiveStartDate + relativedelta(months=+10)
                        GroupChangeState.state = '0'
                        GroupChangeState.g_status = '1'

                        GroupChangeState.save()

                        NewGroup = Group(created_date=datetime.now(), EffectiveStartDate=datetime.now(),EffectiveEndDate=datetime.now(),state='1',g_status='0')
                        NewGroup.save()

                        NewGroup = Group.objects.get(state='1')
                        NweGroupId = NewGroup.group_id

                        for var in range(remainingshare):
                            print('var',var)
                            p3 = Share(group_id_id=NweGroupId, user_id_id=x['UserId'])
                            p3.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewData(APIView):

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        my_list = []

        if serializer.is_valid():
            x = serializer.data
            #value22 = Share.objects.values("group_id_id").distinct().filter(user_id_id=x['UserId'])
            GroupFIlter = Share.objects.filter(user_id_id=x['UserId']).values_list('group_id_id', flat=True).distinct()
            print('GroupFIlter=',GroupFIlter)

            for var in GroupFIlter:
                ObjectGroupTable= Group.objects.get(group_id=str(var))

                DataGroupTableData = {'group_id': ObjectGroupTable.group_id,
                                      'EffectiveStartDate': ObjectGroupTable.EffectiveStartDate,
                                      'EffectiveEndDateEffectiveEndDate': ObjectGroupTable.EffectiveEndDate,
                                      'state': ObjectGroupTable.state,
                                      'g_status': ObjectGroupTable.g_status
                                      }

                if (DataGroupTableData['g_status'] == '1'):

                    DataGroupFinalData = {'group_id': ObjectGroupTable.group_id,
                                          'EffectiveStartDate': ObjectGroupTable.EffectiveStartDate,
                                          'EffectiveEndDateEffectiveEndDate': ObjectGroupTable.EffectiveEndDate,
                                          'state': ObjectGroupTable.state,
                                          'g_status': ObjectGroupTable.g_status
                                          }
                    my_list.append(DataGroupFinalData)
               
            my_json_string = json.dumps(my_list,cls=DjangoJSONEncoder)

            return JsonResponse(my_json_string, status=status.HTTP_201_CREATED,safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareViewData(APIView):

    def post(self, request, format=None):
        serializer = ShareSerializer(data=request.data)
        if serializer.is_valid():
            x = serializer.data

            #ShareGroupTable = Share.objects.filter(user_id_id=x['UserId'],group_id_id=x['GroupId'])

            dict = {
                'ShareGroupTable': list(
                    Share.objects.filter(user_id_id=x['UserId'],group_id_id=x['GroupId']).annotate().values()),
            }

            print(dict)

            return JsonResponse(dict, status=status.HTTP_201_CREATED,safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










