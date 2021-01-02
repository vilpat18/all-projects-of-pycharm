from rest_framework import status

from .serialisers import BankSerializer,BranchSerializer,ClientManagerSerializer,ClientSerializer,\
                           AccountSerializer, DepositSerializer, WithdrawSerializer, TransferSerializer

from .models import Branch , Bank ,Account,Client,ClientManager ,Deposit,Transfer,Withdraw
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class BranchListAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        branch = Branch.objects.all()
        serializer = BranchSerializer(branch,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class BranchDetailAPIView(APIView):

    def get(self,request,pk):
        branch = Branch.objects.get(pk=pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def put(self,request,pk):
        branch = Branch.objects.get(pk=pk)
        serializer = BranchSerializer(branch,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Branch.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BankListAPIView(APIView):

    def get(self,request):
        bank = Bank.objects.all()
        serializer = BankSerializer(bank,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class BankDetailsAPIView(APIView):

    def get(self,request,pk):
        bank = Bank.objects.get(pk=pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    def put(self,request,pk):
        bank = Bank.objects.get(pk=pk)
        serializer = BankSerializer(bank,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Bank.objects.get(pk=pk).delete()
        return Response("successfully deleted!!!!!!")

class AccountAPIView(APIView):

    def get(self,request):
        account = Account.objects.all()
        serializer = AccountSerializer(account,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class AccountDetailsAPIView(APIView):

    def get(self,request,pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self,request,pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Account.objects.get(pk=pk).delete()
        return Response('Successfully Deleted')


class DepositListAPIView(APIView):

    def get(self,request):
        deposit = Deposit.objects.all()
        serializer = DepositSerializer(deposit,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class DepositDetailsAPIView(APIView):

    def get(self,request,pk):
        deposit = Deposit.objects.get(pk=pk)
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)

    def put(self,request,pk):
        deposit = Deposit.objects.get(pk=pk)
        serializer = DepositSerializer(deposit,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Deposit.objects.get(pk=pk).delete()
        return Response('successfully deleted')


class WithdrawListAPIView(APIView):

    def get(self,request):
        withdraw = Withdraw.objects.all()
        serializer = WithdrawSerializer(withdraw,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WithdrawSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class WithdrawDetailsAPIView(APIView):

    def get(self,request,pk):
        withdraw = Withdraw.objects.get(pk=pk)
        serializer = WithdrawSerializer(withdraw)
        return Response(serializer.data)

    def put(self,request,pk):
        withdraw = Withdraw.objects.get(pk=pk)
        serializer = WithdrawSerializer(withdraw,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Withdraw.objects.get(pk=pk).delete()
        return Response('successfully deleted')

class TransferListAPIView(APIView):

    def get(self,request):
        transfer = Transfer.objects.all()
        serializer = TransferSerializer(transfer,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class TransferDetailsAPIView(APIView):

    def get(self,request,pk):
        transfer = Transfer.objects.get(pk=pk)
        serializer = TransferSerializer(transfer)
        return Response(serializer.data)

    def put(self,request,pk):
        transfer = Transfer.objects.get(pk=pk)
        serializer = TransferSerializer(transfer,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk):
        Transfer.objects.get(pk=pk).delete()
        return Response('successfully deleted')


