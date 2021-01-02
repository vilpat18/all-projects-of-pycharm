from rest_framework import serializers


from imageapp.models import Register ,login

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['first_name','last_name','image','email','password','confirm_password','mobile','recovery_email']
        extra_kwargs ={
            'password': {'write_only': True},
            'confirm_password': {'write_only': True} }

        def save(self):
            register = Register (
                 first_name = self.validated_data['first_name'],
                 last_name = self.validated_data['last_name'],
                 email = self.validated_data['email'],
                 mobile = self.validated_data['mobile'],
                 recovery_email = self.validated_data['recovery_email']
                 )
            password = self.validated_data['password'],
            confirm_password = self.validated_data['confirm_password'],
            if password != confirm_password :
                raise serializers.ValidationError({'password': 'password must match'})
            else:
                register.set_password()
                register.save()
            return register


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = login