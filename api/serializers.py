from rest_framework import serializers
from .models import UserProfile,BorderRegistration,MessagesFor,ScannedFaceDt,FingerPrintScanDt

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username','faceDetected', 'fingerPrintCode','fullName', 'profileImage', 'userType', 'number', 'status')


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



class FingerPrintScanDtSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerPrintScanDt
        fields = '__all__'