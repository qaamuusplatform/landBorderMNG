from django.http import Http404
from contextlib import nullcontext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class UserProfileListCreate(APIView):
    """
    List all user profiles or create a new user profile.
    """
    def get(self, request, format=None):
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDetailDelete(APIView):
    """
    Retrieve, update or delete a user profile instance.
    """
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class BorderRegistrationListCreate(APIView):
    """
    List all user profiles or create a new user profile.
    """
    def get(self, request, format=None):
        user_profiles = BorderRegistration.objects.all()
        serializer = BorderRegistrationSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BorderRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BorderRegistrationDetailDelete(APIView):
    """
    Retrieve, update or delete a user profile instance.
    """
    def get_object(self, pk):
        try:
            return BorderRegistration.objects.get(pk=pk)
        except BorderRegistration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = BorderRegistrationSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = BorderRegistrationSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = BorderRegistrationSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MessagesForListCreate(APIView):
    """
    List all user profiles or create a new user profile.
    """
    def get(self, request, format=None):
        user_profiles = MessagesFor.objects.all()
        serializer = MessagesForSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MessagesForSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesForDetailDelete(APIView):
    """
    Retrieve, update or delete a user profile instance.
    """
    def get_object(self, pk):
        try:
            return MessagesFor.objects.get(pk=pk)
        except BorderRegistration.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = MessagesForSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = MessagesForSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = MessagesForSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








def userProfileInfo(request):

    if(request.user.pk==None):
        return {
            'userInfo':{}
        }
    elif(request.user.pk==nullcontext):
        return {
                'userInfo':{}
            }
    else:
        if(UserProfile.objects.filter(theUser=User.objects.get(pk=request.user.pk)).exists()==True):

            return {
                'userInfo': UserProfile.objects.get(theUser=User.objects.get(pk=request.user.pk))
            }
        else:
            return {
                'userInfo': ''
            }
        






class ScannedFaceListCreate(APIView):
    """
    List all user profiles or create a new user profile.
    """
    def get(self, request, format=None):
        user_profiles = ScannedFaceDt.objects.all()
        serializer = ScannedFaceDtSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScannedFaceDtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScannedFaceDetailDelete(APIView):
    """
    Retrieve, update or delete a user profile instance.
    """
    def get_object(self, pk):
        try:
            return ScannedFaceDt.objects.get(pk=pk)
        except ScannedFaceDt.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = ScannedFaceDtSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = ScannedFaceDtSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = ScannedFaceDtSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ScanFingerListCreate(APIView):
    """
    List all user profiles or create a new user profile.
    """
    def get(self, request, format=None):
        user_profiles = FingerPrintScanDt.objects.all()
        serializer = FingerPrintScanDtSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FingerPrintScanDtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScanFingerDetailDelete(APIView):
    """
    Retrieve, update or delete a user profile instance.
    """
    def get_object(self, pk):
        try:
            return FingerPrintScanDt.objects.get(pk=pk)
        except FingerPrintScanDt.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = FingerPrintScanDtSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = FingerPrintScanDtSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = FingerPrintScanDtSerializer(
            user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GetScannedFingerPrint(APIView):
    def get(self, request, format=None):
        theObject=FingerPrintScanDt.objects.all().last()
        serializer=FingerPrintScanDtSerializer(theObject,many=False)
        return Response(serializer.data)