from django.db import models

# Create your models here.
class Policy(models.Model):
    policy_num = models.CharField(max_length=10,unique=True)
    policy_effect_dt = models.DateTimeField()
    policy_expiry_dt = models.DateTimeField()
    payment_option = models.CharField(max_length=100)
    total_amount = models.BigIntegerField()
    active = models.BooleanField(default=False)
    create_dt = models.DateTimeField()


class PolicyEditLog(models.Model):
    policy_id = models.ForeignKey(Policy,on_delete=models.CASCADE)
    edited_by = models.CharField(max_length=100)


class Bill(models.Model):
    due_date = models.DateField()
    min_pay = models.IntegerField()
    balance = models.IntegerField()
    status = models.CharField(max_length=50)

class Payment(models.Model):
    bill_id = models.ForeignKey(Bill,on_delete=models.CASCADE)
    paid_dt = models.DateField()
    amount = models.IntegerField()
    pay_method = models.CharField(max_length=25)
    p_first_name = models.CharField(max_length=50)
    p_last_name = models.CharField(max_length=50)
    card_number = models.IntegerField()
    zip_code = models.IntegerField()
    card_type = models.CharField(max_length=25)
    debit_credit = models.CharField(max_length=25)
    bank_name = models.CharField(max_length=50)
    account_number = models.IntegerField()

class Driver(models.Model):
    policy_id = models.ForeignKey(Policy,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Vehicle(models.Model):
    policy_id = models.ForeignKey(Policy,on_delete=models.CASCADE)
    year = models.DateField()
    model = models.CharField(max_length=50)
    vehicle_num = models.CharField(max_length=50)

class Coverage(models.Model):
    coverage_name = models.CharField(max_length=100)
    coverage_group = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    


