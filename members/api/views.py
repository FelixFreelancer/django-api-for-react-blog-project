from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
)
from rest_framework import permissions
# import models
from members.models import Member
from .serialize import MembersSerializer


class MembersListView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer


class MemberDetailView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer

class MemberCreateView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer

class MemberUpdateView(UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer

class MemberDeleteView(DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MembersSerializer