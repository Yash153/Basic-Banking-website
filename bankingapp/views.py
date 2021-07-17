from django.shortcuts import render
from .models import CustomerModel, TransferModel
from datetime import datetime
from django.core.mail import send_mail
from bankingproject.settings import EMAIL_HOST_USER


# Create your views here.
def home(request):
	return render(request, "home.html")

def createcustomer(request):
	if request.method == "POST":
		n = request.POST.get('name')
		em = request.POST.get('email')
		b = request.POST.get('balance')
		d = CustomerModel(name = n, email = em, balance = b)
		d.save()
		send_mail("Welcome to MyBank", "Dear " + n + ",\nThank you for creating a account in our bank\nYour current account balance is \u20B9."+b, EMAIL_HOST_USER, [em])

		return render(request, 'createcustomer.html', {'msg' : 'Customer added'})
	else:
		return render(request, 'createcustomer.html')

def viewcustomer(request):
	data = CustomerModel.objects.all()
	return render(request, 'viewcustomer.html', {'data' : data})

def view(request, id):
	data = CustomerModel.objects.get(pk = id)
	return render(request, 'view.html', {'data' : data})

def contact(request):
	if request.method == "POST":
		n = request.POST.get('name')
		e = request.POST.get('email')
		f = request.POST.get('feedback')
		send_mail("Feedback from "+n,"Email id : "+e+"\nFeedback : "+f,EMAIL_HOST_USER,['yashash315.ys@gmail.com'])
		return render(request,'contact.html',{'msg' : "Thanks for providing your\nvaluable feedback"})
	else:
		return render(request,'contact.html')
def transfer(request):
	if request.method == "POST":
		data = CustomerModel.objects.all()
		print(data)

		
		sender_id = request.POST.get('account_sender')
		print(sender_id)

		receiver_id = request.POST.get('account_receiver')
		print(receiver_id)
			
		transfer_amount = (float)(request.POST.get('transfer_amount'))
	
		if(receiver_id == None or sender_id == None):
			return render(request, 'transfer.html', {'data' : data, 'msg' : 'Please select customer'})
		elif(sender_id == receiver_id):
			return render(request, 'transfer.html', {'data' : data, 'msg' : 'Please select different accounts'})
		elif(transfer_amount > (CustomerModel.objects.filter(id = sender_id).values('balance'))[0]['balance']):
			return render(request, 'transfer.html', {'data' : data, 'msg' : 'Insufficient Funds'})
		else:	
			sender_email = CustomerModel.objects.filter(id = sender_id).values('email')
			sender_email = sender_email[0]['email']

			receiver_email = CustomerModel.objects.filter(id = receiver_id).values('email')
			receiver_email = receiver_email[0]['email']


			sender_balance = CustomerModel.objects.filter(id = sender_id).values('balance')
			sender_balance = sender_balance[0]['balance']

			receiver_balance = CustomerModel.objects.filter(id = receiver_id).values('balance')
			receiver_balance = receiver_balance[0]['balance']


			updated_sender = round((sender_balance - transfer_amount), 3)
			sub = CustomerModel.objects.filter(id = sender_id).update(balance = updated_sender)
			updated_receiver = round((receiver_balance + transfer_amount), 3)
			rub = CustomerModel.objects.filter(id = receiver_id).update(balance = updated_receiver)
	
			sender_name = CustomerModel.objects.filter(id = sender_id).values('name')
			sender_name = sender_name[0]['name']
			print(sender_name)	

			receiver_name = CustomerModel.objects.filter(id = receiver_id).values('name')
			receiver_name = receiver_name[0]['name']
			print(receiver_name)
	
			now = datetime.now()
			dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
			print("date and time =", dt_string)
	
			d = TransferModel(sender = sender_name, receiver = receiver_name, amount = transfer_amount, dt = dt_string)	
			d.save()

			send_mail("Debit Transaction", "Dear " + sender_name + ",\nYour account has been debited by \u20B9." + str(transfer_amount) + " and available balance is \u20B9." + str(updated_sender), EMAIL_HOST_USER, [sender_email])

			send_mail("Credit Transaction", "Dear " + receiver_name + ",\nYour account has been credited by \u20B9." + str(transfer_amount) + " and available balance is \u20B9." + str(updated_receiver) , EMAIL_HOST_USER, [receiver_email])
	

			return render(request, 'transfer.html', {'data' : data, 'msg' : 'Transfer Completed'})
	else:
		data = CustomerModel.objects.all()
		return render(request, 'transfer.html', {'data' : data})

def transferhistory(request):
	if request.method == "POST":
		data = CustomerModel.objects.all()
		account_id = request.POST.get('history')
		# print(email)
		if (account_id == None):
			return render(request, 'transferhistory.html', {'msg' : 'Please select customer', 'data' : data})
		else:
			account_name = CustomerModel.objects.filter(id = account_id).values('name')
			account_name = account_name[0]['name']
			
			debit_history = TransferModel.objects.filter(sender = account_name)
			credit_history = TransferModel.objects.filter(receiver = account_name)	
			return render(request, 'transferhistory.html', {'data' : data, 'debit_history' : debit_history, 'credit_history' : credit_history})
	else:
		data = CustomerModel.objects.all()
		return render(request, 'transferhistory.html', {'data' : data})