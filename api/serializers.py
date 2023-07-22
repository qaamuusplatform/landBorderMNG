from rest_framework import serializers
from .models import UserProfile,BorderRegistration,MessagesFor

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username','faceDetected', 'fullName', 'profileImage', 'userType', 'number', 'status')


class BorderRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorderRegistration
        fields = '__all__'

class MessagesForSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesFor
        fields = '__all__'