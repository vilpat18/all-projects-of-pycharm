from rest_framework import serializers
from restapp.models import Employee

def multiples_of_1000(value):
    if value %1000 !=0:
        raise serializers.ValidationError('sal shd b multpl of 1000')

class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000]) #for validation we have to mention field name expecitly
    class Meta:
        model = Employee
        fields = '__all__'

'''class EmployeeSerializer(serializers.serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[multiples_of_1000])
    eadd = serializers.CharField(max_length=64)
    def validate_esal(self,value): #field level validation
        if value<5000:
            raise serializers.ValidationError('emp sal shld be min 5000')
        return value
    def validate(self,data): #object level validation
        ename=data.get('ename')
        esal = data.get('esal')
        if ename.lower()=='ajay':
            if esal<5000:
                raise serializers.ValidationError('ajy salry shd b min 5000')
        return data

    def create(self,validated_data):# post opertaion
        return Employee.objects.create(**validated_data) #validated_data means partner app or enduser providing data
    def update(self,instance,validated_data):# instance means current existing object present in the database
        instance.eno = validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('ename',instance.ename)
        instance.esal = validated_data.get('esal',instance.esal)
        instance.eadd = validated_data.get('eadd',instance.eadd)
        instance.save()
        return instance'''
