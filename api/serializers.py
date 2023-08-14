from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username','faceDetected','fullName', 'profileImage','passportID', 'userType', 'number', 'status')


class ScannedFaceDtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedFaceDt
        fields = '__all__'


class BorderRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorderRegistration
        fields = '__all__'

class MessagesForSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesFor
        fields = '__all__'

class FinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fines
        fields = '__all__'

class ExtraTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraTime
        fields = '__all__'

class FingerPrintScanDtSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerPrintScanDt
        fields = '__all__'