from Account.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta: 
    model = User
    fields = '__all__'

# class FeeSerializer(serializers.ModelSerializer):
#   class Meta: 
#     model = Fee
#     fields = ('totalFee')

# class ScholarshipSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Scholarship
#     fields = '__all__'


# class PaymentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Payment
#     fields = ('payment')