from django.contrib import admin

# Register your models here.
from .models import Policy,PolicyEditLog,Bill,Payment,Driver,Vehicle,Coverage

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['id','policy_num','policy_effect_dt','policy_expiry_dt',
                  'payment_option','total_amount','active','create_dt']


@admin.register(PolicyEditLog)
class PolicyEditAdmin(admin.ModelAdmin):
    list_display = ['id','policy_id','edited_by']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id','due_date','min_pay', 'balance','status']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','bill_id','paid_dt','amount',
                  'pay_method','p_first_name','p_last_name','card_number','zip_code',
                  'card_type','debit_credit','bank_name','account_number']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id','policy_id','first_name', 'last_name','email']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id','policy_id','year', 'model','vehicle_num']


@admin.register(Coverage)
class CoverageAdmin(admin.ModelAdmin):
    list_display = ['id','coverage_name','coverage_group', 'code']