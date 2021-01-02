from rest_framework import serializers

from regapp.models import Register

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password2'},write_only=True)

    class Meta:
        model = Register
        fields = ['first_name','last_name','username','email','password1','password2','mobile','recovery_email']
        extra_kwargs = {
            'password1':{'write_only':True}
        }

    def save(self):
        register = Register(
                   email = self.validated_data['email'],
                   username = self.validated_data['username']
        )
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']

        if password1 != password2 :
            raise serializers.ValidationError({'password':'passwords must match'})
        register.set_password(password1)
        register.save()
        return register
