from rest_framework import serializers

# import models
from members.models import Member
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'content')