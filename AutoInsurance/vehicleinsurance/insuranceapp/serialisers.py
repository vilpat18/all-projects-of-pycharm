from .models import Policy,PolicyEditLog,Bill,Payment,Driver,Vehicle,Coverage
from rest_framework import serializers

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['id','policy_num','policy_effect_dt','policy_expiry_dt',
                  'payment_option','total_amount','active','create_dt']


class PolicyEditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyEditLog
        fields = ['id','policy_id','edited_by']


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id','due_date','min_pay', 'balance','status']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','bill_id','paid_dt','amount',
                  'pay_method','p_first_name','p_last_name','card_number','zip_code',
                  'card_type','debit_credit','bank_name','account_number']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id','policy_id','first_name', 'last_name','email']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','policy_id','year', 'model','vehicle_num']


class CoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coverage
        fields = ['id','coverage_name','coverage_group', 'code']





















