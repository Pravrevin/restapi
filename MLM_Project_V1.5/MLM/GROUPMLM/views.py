from . serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Group , Share
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from django.http import Http404
from .serializers import GroupViewForUsersSerializer ,GroupSerializer
from MLMAPP.models import MyUser
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection


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


class GroupViewForUsers(APIView):

    def get_object(self, pk):
        try:
            return Share.objects.get(pk=pk)
        except Share.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        value = Share.objects.values("group_id_id").distinct().filter(user_id_id=x['UserId'])
        print('value',value)
        serializer = GroupViewForUsersSerializer(snippet)

        return Response(serializer.data)

class GroupViewData(APIView):

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        cursor = connection.cursor()
        data =cursor.execute('''SELECT count(*) FROM Group''')
        print(data)

        if serializer.is_valid():
            #serializer.save()
            x = serializer.data
            #value22 = Share.objects.values("group_id_id").distinct().filter(user_id_id=x['UserId'])
            GroupFIlter = Share.objects.filter(user_id_id=x['UserId']).values_list('group_id_id', flat=True).distinct()

            print('GroupFIlter=',GroupFIlter)
            my_list=[]



            '''
            for var in GroupFIlter:
                print(var,type(var))
                #ObjectGroupTable = Group.objects.filter(g_status='1')| Group.objects.filter(group_id=str(var))
                ObjectGroupTable = Group.objects.raw('select * from Group')
                print(ObjectGroupTable)


                DataGroupTableData ={'group_id':ObjectGroupTable.group_id,'EffectiveStartDate':ObjectGroupTable.EffectiveStartDate,
                                         'EffectiveEndDateEffectiveEndDate':ObjectGroupTable.EffectiveEndDate,'state':ObjectGroupTable.state,
                                         'g_status':ObjectGroupTable.g_status
                                         }

                #print(DataGroupTableData)
                my_list.append(DataGroupTableData)
            print(my_list,type(my_list))
            my_json_string = json.dumps(my_list,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
            '''


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







