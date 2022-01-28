from django.shortcuts import render, redirect
from .forms import EmployeeForm
from employee.models import Employee_skill
from manager.decoretors import allowed_users
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def employee_list(request):
    try:
        if (request.user.groups.all()[0].name == "employee"):
            context = {'employee_list': User.objects.filter(
            id=request.user.id),'user_type' : 'employee'}
            return render(request, "employee_register/employee_list.html", context)
        else:
            context = {'employee_list': User.objects.filter(
            groups__name='employee')}
            return render(request, "employee_register/employee_list.html", context)
    except:
        return redirect('/logout/')
    
# @allowed_users(allowed_roles=['admin','manager'])
@login_required(login_url='/login/')
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
            return render(request, "employee_register/employee_form.html", {'form': form,})
        else:
            employee = User.objects.get(id=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = User.objects.get(id=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            value = form.save()
            my_group = Group.objects.get(name='employee') 
            my_group.user_set.add(value)
        return redirect('/employee/list/')

@login_required(login_url='/login/')
def employee_delete(request,id):
    employee = User.objects.get(id=id)
    employee.delete()
    return redirect('/employee/list/')

@login_required(login_url='/login/')
def profile(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()

            return render(request, "employee_register/employee_profile.html", {'form': form,})
        else:
            employee = User.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_profile.html", {'form': form,'employee_id':id})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            value = form.save()
            my_group = Group.objects.get(name='employee') 
            my_group.user_set.add(value)
        return redirect('/employee/list/')

@login_required(login_url='/login/')
def skill_details(re):
    add_emp_exp_details = Employee_skill(emp_id=re.POST['employee_id'], skills=re.POST["skill"], percentage=re.POST["percentage"])
    add_emp_exp_details.save()
    if(re.POST["skill_len"] != ""):
        for i in range(1, (int(re.POST["skill_len"])+1)):
            try:
                BO_1 = Employee_skill(emp_id=re.POST['employee_id'], skills=re.POST["skill"+str(i)], percentage=re.POST["percentage"+str(
                    i)])
                BO_1.save()
            except:
                continue
    return redirect('/employee/list/')

@login_required(login_url='/login/')
def skill_chart(request,id=0):
    labels = []
    data = []
    print ()
    queryset = Employee_skill.objects.filter(emp_id=id).values()
    for entry in queryset:
        labels.append(entry['skills'])
        data.append(entry['percentage'])
      
    return render(request,"employee_register/skill_chart.html", {'labels' : labels,'data' : data})


   