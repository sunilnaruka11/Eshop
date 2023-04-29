from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View 
# import Models  
from store.models.customer import Customer


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
	
    def post(self, request):
            PostData =request.POST
            Email = PostData.get('email')
            Password = PostData.get('password')
            customerdata = self.get_customer_by_email(Email)
           
            error_message = None

            if customerdata:
                flag = check_password(Password, customerdata.password)
                
                if flag:
                    ID = request.session['CUSTOMERID']=customerdata.id
                    EMAIL = request.session['CUSTOMEREMAIL']=customerdata.email
                    
                   # return redirect(f'/homepage/{EMAIL}')
                    return redirect('homepage')
                else:    
                    error_message = ' Password invalid !!'
                    data = {'error':error_message}
                    return render(request, 'login.html', data)
            else:
                 error_message = 'Email invalid !!'
                 data = {'error':error_message}
                
                 return render(request, 'login.html', data)

    def get_customer_by_email(self,Email):
            try:
                return Customer.objects.get(email=Email)
            except:
                return False

           
           
            


    