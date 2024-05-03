from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from auth_user.models import User, Profile
from rest_framework.permissions import IsAuthenticated



class Singup(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Singup'})
    

    def post(self, req: Request):
        phone = req.data.get('phone')
        password = req.data.get('password')

        user = User.objects.create(phone=phone, password=password)
        Profile.objects.create(user=user)

        token = RefreshToken.for_user(user)

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })
    


class Singin(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Singin'})
    

    def post(self, req: Request):
        phone = req.data.get('phone')
        password = req.data.get('password')

        user = User.objects.all().filter(phone=phone, password=password).first()

        token = RefreshToken.for_user(user)

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token)
        })
    

class ProfileEdit(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req: Request):
        return Response({'msg': 'Profile editing'})
    
    def post(self, req: Request):
        name = req.data.get('name')
        data = req.data.get('data')
        profile = Profile.objects.get(user=req.user)

        if name == 'image':
            profile.img = data
            profile.save()

        elif name == 'first_name':
            profile.first_name = data
            profile.save()

        elif name == 'last_name':
            profile.lastt_name = data
            profile.save()

        elif name == 'birthday':
            profile.birthday = data
            profile.save()         

        else:
            return Response({'msg': 'Something went wrong !!!'})
        
        return Response({'Succes': True})