from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View 
# import Models  
from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
	
    def post(self, request):
            PostData =request.POST
            FirstName = PostData.get('firstname')
            LastName =  PostData.get('lastname')
            Mobile =    PostData.get('phone')
            Email =     PostData.get('email')
            Pasword =   PostData.get('password')
            # Create Dict for singup form value
            value = {
                'first_name': FirstName,
                'last_name': LastName,
                'phone': Mobile,
                'email': Email
            }
            # Create Customer Object 
            PaswordEnCript= make_password(Pasword)
            customer = Customer(first_name=FirstName,last_name=LastName,phone=Mobile,email=Email,password=PaswordEnCript)
            # Validation Customer Object
            error_message = None
            error_message = self.validateCustomer(customer)  
            # Save Customer Object if not error 
            if not error_message: 
                customer.save()
                return redirect('homepage')
            else:
                data = {'error':error_message,'values':value }
                return render(request, 'signup.html', data)


    def validateCustomer(self,customer):
            error_message = None
            Email1 = self.isExistsEmail(customer.email)
            if (not customer.first_name):
                error_message = "First Name Required !!"
            elif len(customer.first_name) < 4:
                error_message = 'First Name must be 4 char long or more !!'
            elif (not customer.phone):
                error_message = "Phone Number required !!"
            elif len(customer.phone) < 10:
                error_message = 'Phone Number must be 10 char long !!'
            elif (Email1==True):
                error_message = 'Email Address Already Registered.!!'	
            
            return error_message

    def isExistsEmail(self,EmailID):
            EmailData = Customer.objects.filter(email=EmailID)
            if EmailData:
                return True
            else:
                return False	
	