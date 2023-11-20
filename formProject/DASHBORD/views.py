from django.shortcuts import render , redirect
from form.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def show_form(e , formname):
    form = Form.objects.filter(name__contains = formname).first()
    return render(e , "form/home.html" ,{'form':form})



@login_required(login_url="authapp:login")
def home(e):
    forms = Form.objects.all()
    if e.method == "POST":
        print(e.POST)
        # create the form
        newfrom = Form.objects.create(
            name    = e.POST['name'],
            color   = e.POST.get('bgcolor'),
            image   = e.FILES.get('bgimage'),
            logo    = e.FILES.get('headerImage'),
            state   = True
        )
        # cretae the instractions 
        newInstr = instractions.objects.create(
            Name    = e.POST.get('name'),
            Title   = e.POST.get('title'),
            Text    = e.POST.get('text'),
            header  = e.POST.get('instraction-header'),
            form    = newfrom
        )
        if e.POST.get('point'):
            for point in e.POST.getlist('point'):
                Points.objects.create(
                    instractions = newInstr,
                    text         = point
                )
        # Create Answer
        if e.POST.get('field'):
            for index,i in enumerate(e.POST.getlist('field')): 
                print(index , i , e.POST.getlist('input-header')[0] , e.POST.get('input-header'))
                newField = Fiald.objects.create(
                    headercolor     = e.POST.getlist('input-header')[index],
                    Form            = newfrom,
                    question        = e.POST.getlist('input-question')[index],
                    video           = e.FILES.getlist('video')[index] if 'video' in e.POST else None,
                    answer          = answer.objects.create(name = e.POST.getlist('answer-name')[index] , text = True),
                )
    
    return render(e , 'DASHBORD/home.html' , {'forms':forms})

@login_required(login_url="authapp:login")
def show_form_data(e , formName = None):
    form = Form.objects.filter(name__contains = formName).first()
    allFeailds = form.get_all_fiald(with_connection=True)
    data = DataBase.objects.filter(form = form).order_by('-id')
    return render(e , "DASHBORD/data.html" , {'form':form , 'feailds':allFeailds , 'data':data})

@login_required(login_url="authapp:login")
def edit_form(e,formname):
    form = Form.objects.filter(name = formname).first()
    if e.method == "POST":
        if 'delete' in e.POST:
            targetFiald  = Fiald.objects.get(id = e.POST['delete'])
            targetAnswer = answer.objects.get(id = targetFiald.answer.id)
            targetFiald.delete() ; targetAnswer.delete()

            return redirect(f"/dashbord/edit/{formname}")
        # changing on the form  if it there with .get
        form.logo       = e.FILES.get('logo') if e.FILES.get('logo') else form.logo
        form.next_step  = True if  e.POST.get('next') == "on" else False
        form.image      = e.FILES.get('form-image') if e.FILES.get('form-image') else form.image
        form.color      = e.POST.get('form-color')

        if 'feaild-name' in e.POST:
            # create answer for the question 
            ans = answer.objects.create(
                name            = e.POST.get('answer-name'),
                text            = True if not e.POST.get('is-mcq') == "on" else False,
                msq             = True if     e.POST.get('is-mcq') == 'on' else False
                )
            #  create the fiald object 
            newFeaild = Fiald.objects.create(
                headercolor     = e.POST.get('headercolor') or "#f2f2f2",
                Form            = form,
                question        = e.POST.get('feaild-name'),
                answer          = ans
                )
            # check for the connections 
            if e.POST.get('connections' , 'none') != 'none':
                newFeaild.connection.set(
                e.POST['connections']
                )
                newFeaild.form = None
            
            #! Loop for All the MCq Points 
            if e.POST.get('is-mcq') == 'on':
                for point in e.POST.getlist('mcq-point'):
                    Mcq.objects.create(
                        answer      = ans,
                        text        = point
                    )
        form.save()
        print(e.POST)
    return render(e , "DASHBORD/edit.html" , {"form":form})

def get_old_forms(e , uuid = None):
    try:
        data = DataBase.objects.filter(UUid = uuid).first()
        form = Form.objects.get(id = data.form.id)
        fields = [i[0] for i in data.get_all_values().values_list("value")[1:]]
        print(fields)
    except Exception as error:
        print(error)
        e.session.clear()
        return redirect("form:home")
    return render(e , "DASHBORD/oldata.html" , {"form":form , "data":data , "fields":fields})
