from queryapp.models import Employee,Manager,Contact_info

from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact_info
        fields = ('phone','email','address')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        modal = Employee
        fields = ('e_name','e_salary','e_contact_info')


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ('m_name','m_salary','m_contact_info')




