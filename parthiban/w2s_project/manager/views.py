from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .decoretors import allowed_users
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def change_password(request):
    if request.method == 'POST':
        form = passwordchangingform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordchangingform(request.user)
    return render(request, 'change password/change_password.html', {
        'form': form
    })

def login_1(re):
    if (re.method == "GET"):
        return render(re, 'login.html')
    else:
        get_employee_id = re.POST['log_emp_id']
        get_employee_password = re.POST['log_password']
        user = authenticate(username=get_employee_id,
                            password=get_employee_password)
        if user is not None:
           
            login(re, user)
         
            re.session["upload_emp_id"] = str(user)
            print(re.session.get("upload_emp_id"))
            # if (re.user.groups.all()[0].name == "employee"):
            #     context = {'employee_list': User.objects.filter(id=re.user.id)}
            #     return render(re, "employee_register/employee_list.html", context)

            return redirect('/Dashboard/')
        else:
            messages.success(re, 'Invalid username or password.')
            return render(re, 'login.html')

def logout_1(re):
    logout(re)
    return redirect('/login/')

@login_required(login_url='/login/')
def home(re):
    get_session_value_id = re.session.get("upload_emp_id")
    get_user_name = User.objects.all()
    get_user_is_staff_or_not = re.user.is_staff
    user_is_admin_or_not = list(re.user.groups.filter().values_list(flat = True))
    return render(re, 'forms.html', {"dashboard_check": "dashboard_check"})

