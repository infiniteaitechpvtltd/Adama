import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
import datetime
from dateutil.relativedelta import relativedelta
import pyodbc
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import UserDetailsForm
from django.template.defaulttags import register
from django.core.files.storage import FileSystemStorage
import ast
from django.contrib.auth.decorators import login_required
from .process import html_to_pdf
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers

# def decor(func):
#     print("in decor")


def db_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};;SERVER=192.168.232.243,1433;DATABASE=Project;UID=adama-db;PWD=Adama$QL22')
    cursor = conn.cursor()
    return cursor


def notification(group_name, type):


    noti=notifications_db.objects.values(group_name)


    noti_list = ast.literal_eval(noti[0][group_name])

    if type == "view":
        notifications = [
            {"count": len(noti_list)},
            {"content":noti_list}
        ]
        return notifications
    elif type[0] == "create":
        noti_list.append(
            {
                "username":type[1],
                "comment":type[2],
                "view":type[3],
                "url":type[4],
            }
        )

        get_noti = notifications_db.objects.get(id=1)
        if group_name == "formulation_operator":
            get_noti.formulation_operator = noti_list
        elif group_name == "packaging_operator":
            get_noti.packaging_operator = noti_list
        elif group_name == "formulation_shiftincharge":
            get_noti.formulation_shiftincharge = noti_list
        elif group_name == "packaging_shiftincharge":
            get_noti.packaging_shiftincharge = noti_list
        elif group_name == "formulation_lineincharge":
            get_noti.formulation_lineincharge = noti_list
        elif group_name == "packaging_lineincharge":
            get_noti.packaging_lineincharge = noti_list
        else:
            print("no notification")

        get_noti.save()

        notifications = [
            {"count": len(noti_list)},
            {"content": noti_list}
        ]
        return notifications

def delete_notification(request, data):
    group_name= role_checker(request,"home")[1]
    get_noti = notifications_db.objects.get(id=1)
    if group_name == "formulation_operator":
        noti_list = ast.literal_eval(get_noti.formulation_operator)
        noti_list.remove(ast.literal_eval(data))
        get_noti.formulation_operator = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_operator":
        noti_list = ast.literal_eval(get_noti.packaging_operator)
        noti_list.remove(ast.literal_eval(data))
        get_noti.packaging_operator = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "formulation_shiftincharge":
        noti_list = ast.literal_eval(get_noti.formulation_shiftincharge)
        noti_list.remove(ast.literal_eval(data))
        get_noti.formulation_shiftincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_shiftincharge":
        noti_list = ast.literal_eval(get_noti.packaging_shiftincharge)
        noti_list.remove(ast.literal_eval(data))
        get_noti.packaging_shiftincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "formulation_lineincharge":
        noti_list = ast.literal_eval(get_noti.formulation_lineincharge)
        noti_list.remove(ast.literal_eval(data))
        get_noti.formulation_lineincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_lineincharge":
        noti_list = ast.literal_eval(get_noti.packaging_lineincharge)
        noti_list.remove(ast.literal_eval(data))
        get_noti.packaging_lineincharge = noti_list
        get_noti.save()
        return redirect(home)
    else:
        print("no notification")
        return redirect(home)


def delete_all_notification(request):
    group_name= role_checker(request,"home")[1]
    get_noti = notifications_db.objects.get(id=1)
    if group_name == "formulation_operator":
        noti_list = ast.literal_eval(get_noti.formulation_operator)
        noti_list = []
        #noti_list.remove(ast.literal_eval(data))
        get_noti.formulation_operator = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_operator":
        #noti_list = ast.literal_eval(get_noti.packaging_operator)
        noti_list = []
        #print("noti_list", get_noti.packaging_operator)
        #noti_list.remove(ast.literal_eval(data))
        get_noti.packaging_operator = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "formulation_shiftincharge":
        #noti_list = ast.literal_eval(get_noti.formulation_shiftincharge)
        noti_list = []
        #noti_list.remove(ast.literal_eval(data))
        get_noti.formulation_shiftincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_shiftincharge":
        #noti_list = ast.literal_eval(get_noti.packaging_shiftincharge)
        #noti_list.remove(ast.literal_eval(data))
        noti_list = []
        get_noti.packaging_shiftincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "formulation_lineincharge":
        #noti_list = ast.literal_eval(get_noti.formulation_lineincharge)
        #noti_list.remove(ast.literal_eval(data))
        noti_list = []
        get_noti.formulation_lineincharge = noti_list
        get_noti.save()
        return redirect(home)
    elif group_name == "packaging_lineincharge":
        #noti_list = ast.literal_eval(get_noti.packaging_lineincharge)
        #noti_list.remove(ast.literal_eval(data))
        noti_list = []
        get_noti.packaging_lineincharge = noti_list
        get_noti.save()
        return redirect(home)
    else:
        print("no notification")
        return redirect(home)

def role_checker(request,access_request):

    user_data = User_Data.objects.filter(Username=str(request.user))
    if str(request.user) == "admin":
        group_name = "admin"
    else:
        if len(user_data) != 0:
            user_role = user_data[0].User_Role
            user_process = user_data[0].process
            if user_role == "Operator" and user_process == "Formulation":
                group_name = "formulation_operator"
            elif user_role == "Operator" and user_process == "Packaging":
                group_name = "packaging_operator"
            elif user_role == "Shift Incharge" and user_process == "Formulation":
                group_name = "formulation_shiftincharge"
            elif user_role == "Shift Incharge" and user_process == "Packaging":
                group_name = "packaging_shiftincharge"
            elif user_role == "Line Incharge" and user_process == "Formulation":
                group_name = "formulation_lineincharge"
            elif user_role == "Line Incharge" and user_process == "Packaging":
                group_name = "packaging_lineincharge"
            else:
                group_name = "a_user"
        else:
            group_name = "a_user"

    formulation_operator_access = ["home", "task","manpower","sop","maintenance","edit_maintenance","delete_maintenance","view_maintenance","create_maintenance","alarm","profile","formulation_module","batchcard","create_batchcard","edit_batchcard","view_batchcard","draft_batchcard",
                                   "view_receipe","add_chemicals","add_view_chemicals","delete_batchcard"]
    formulation_shift_incharge_access = ["home","create_task", "task","manpower","sop","maintenance","alarm","profile","formulation_module", "batchcard", "batchcard_status", "edit_batchcard", "view_batchcard",
                                         "draft_batchcard", "view_receipe","add_view_chemicals", "view_chemicals"]
    formulation_line_incharge_access = ["home","create_task", "task","manpower","sop","maintenance","alarm","profile","formulation_module", "batchcard", "view_batchcard","add_view_chemicals", "view_chemicals", "view_package",
                                        "view_production"]

    packaging_operator_access = ["home", "task","manpower","sop","maintenance","edit_maintenance","delete_maintenance","view_maintenance","create_maintenance","alarm","profile","packaging_module", "create_package", "edit_package","view_package", "draft_package",
                                 "delete_package", "add_package", "add_production","view_production"]
    packaging_shift_incharge_access = ["home","create_task", "task","manpower","sop","maintenance","alarm","profile","packaging_module","packagecard_status","edit_package", "view_package","draft_package", "delete_package", "package_status",
                                       "view_production"]
    packaging_line_incharge_access = ["home","create_task","task","manpower","sop","maintenance","alarm","profile","packaging_module", "batchcard", "view_batchcard", "view_chemicals","add_view_chemicals", "view_package", "view_production"]

    admin_access = ["home","create_task", "task","manpower","sop","maintenance","edit_maintenance","delete_maintenance","view_maintenance","create_maintenance","alarm","profile", "formulation_module", "packaging_module", "batchcard", "batchcard_status", "create_batchcard", "edit_batchcard","view_batchcard","draft_batchcard",
                    "delete_batchcard","view_receipe","add_chemicals","view_chemicals","add_view_chemicals","create_package","edit_package","view_package","draft_package",
                    "delete_package","package_status","add_package","view_package","add_production","view_production"]

    if group_name=="formulation_operator" and access_request in formulation_operator_access:
        return formulation_operator_access,group_name
    elif group_name=="packaging_operator" and access_request in packaging_operator_access:
        return packaging_operator_access,group_name
    elif group_name=="formulation_shiftincharge" and access_request in formulation_shift_incharge_access:
        return formulation_shift_incharge_access,group_name
    elif group_name=="packaging_shiftincharge" and access_request in packaging_shift_incharge_access:
        return packaging_shift_incharge_access,group_name
    elif group_name=="formulation_lineincharge" and access_request in formulation_line_incharge_access:
        return formulation_line_incharge_access,group_name
    elif group_name=="packaging_lineincharge" and access_request in packaging_line_incharge_access:
        return packaging_line_incharge_access,group_name
    elif group_name=="admin":
        return admin_access,group_name
    else:
        return False,group_name


def no_access(request):
    return render(request,"no_access.html")


def signin(request):
    msg = ""
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            if username == "":
                msg = "Username Incorrect"
            elif password == "":
                msg = "Password Incorrect"
            elif user is None:
                msg = "Username & Password Incorrect"

            return render(request, 'auth-login.html',{"username":username, "password":password, "msg":msg})
    return render(request, 'auth-login.html',{"msg":msg})


def signout(request):
    print("User Logging Out")
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def home(request):
    cursor = db_connection()
    user_permissions = role_checker(request, "home")[0]
    notifications = notification(role_checker(request, "home")[1],"view")
    #create = ["create",request.user,"Batch_Card Approved",""]
    #notifications = notification(role_checker(request, "home")[1],create)
    plant_list = Plant_List.objects.all()
    print(plant_list[0].LineDetails)
    batchcard_count = Batch_Card.objects.filter(BatchCard_Approval="InProgress").count()
    packagecard_count = PackageCard.objects.filter(PackageCardApproval="InProgress").count()

    plant_names = cursor.execute("""SELECT DISTINCT[Plant_Name] FROM[Project].[dbo].[HerbicideOEEData]""")
    plant = [i[0] for i in plant_names]
    print('plant', plant)
    line_no = []

    for j in plant:
        line = cursor.execute(
            """ SELECT [LineNo] FROM [Project].[dbo].[HerbicideOEEData] WHERE [Plant_Name] = ? AND [Line_Status] = 1""",
            j)
        # print('line',type(line))
        lineno_list = [k[0] for k in line]
        print('lineno_list', j, lineno_list)
        line_no.append(lineno_list)
    print('line_no', line_no)

    plant_lineno = dict(zip(plant, line_no))
    print('json', plant_lineno)

    json = {
        'notifications': notifications,
        'user_permissions': user_permissions,
        'batchcard_count': batchcard_count,
        'packagecard_count': packagecard_count,
        'plant_list': plant_list,
        "plant_details":plant_lineno
            # {
            #     'Herbicide': ["FM301", "FM302", "FM303", "FM304", "FM305", "FM306", "FM401", "FM402"],
            #     'Insecticide1': ["FM101", "FM102", "FM103", "FM104", "FM105"],
            #     "Insecticide2": ["FM701", "FM702", "FM703", "FM801A", "FM801B", "FM801C", "FM801D", "FM404"],
            #     "WDG": ["FM1001"],
            #     "NIMITZ": ["FM901"]
            # }
    }
    return render(request, 'index.html', json)

@csrf_exempt
def home_ajax(request):
    keys = ["LineNo","PackageCardNo","availability","performance","quality","oee","std_op","break_time","prod_time","actual_prod"]

    data = {}

    if request.method == "POST":
        plant_name = request.POST["plantname"]
        lineno = request.POST["lineno"]
        msdata = oee_mssql(plant_name, lineno)

        print("msdataa", msdata)

        if msdata == None or len(msdata) == 0:
            msdata = [(lineno,"0","0","0","0","0","0","0","0","0")]

        for i in range(0,len(keys)):
            #print("iiiiiii",i)
            print("msdataaaaaa", msdata)
            data.update({keys[i]:msdata[0][i]})
        #print(data)
    return JsonResponse(data)


def oee_mssql(plant_name, LineNo):
    cursor = db_connection()
    # conn = pyodbc.connect(
    #     'DRIVER={SQL Server};;SERVER=192.168.232.243,1433;DATABASE=Project;UID=adama-db;PWD=Adama$QL22')
    # cursor = conn.cursor()
    qs = "HerbicideOEEData"
    #"""select * from BatchDetails where [LineNo] = ? """, LineNo
    #query0 = """SELECT * FROM"""+ qs+ """WHERE [LineNo]=? """, LineNo
    cursor.execute("""SELECT * FROM """+ qs+ """ WHERE [LineNo]=? """, LineNo)
    result = cursor.fetchall()
    print("result", result)
    return result

@login_required(login_url='login')
def batchcard(request):
    user_permissions = role_checker(request, "batchcard")[0]
    notifications = notification(role_checker(request, "batchcard")[1],"view")

    if user_permissions is False:
        return redirect(no_access)

    batchcards_list = Batch_Card.objects.all()

    return render(request, 'batchcard.html', {'batch_list': batchcards_list,'notifications':notifications,'user_permissions':user_permissions})


@login_required(login_url='login')
def newbatchcard(request):

    user_permissions = role_checker(request, "create_batchcard")[0]
    notifications = notification(role_checker(request, "create_batchcard")[1],"view")

    if user_permissions is False:
        return redirect(no_access)

    date = datetime.date.today()
    pc = []
    chemical_list = []


    for i in Chemical.objects.values_list('product_category').distinct():
        pc.append(i[0])
    # print("pc", pc)

    for i in Chemical.objects.values_list("Brand_Name"):
        chemical_list.append(i[0])
    # print("chemical_list",chemical_list)

    data = {
        "shift": Shift.objects.all(),
        "Tanks": Tank.objects.all(),
        "Chemicals": chemical_list,
        "date": date,
        "pc":pc
    }

    if request.method=="GET" and "pc" in request.GET:
        Chemicals=[]
        data = request.GET["pc"]
        for i in Chemical.objects.filter(product_category=data).values("Brand_Name"):
            Chemicals.append(i["Brand_Name"])
        Chemicals={"Chemical":Chemicals}
        return JsonResponse(Chemicals)

    if request.method == 'POST' and 'form1' in request.POST:
        product_category = request.POST['product_category']
        brand_name = request.POST['brand_name']
        batch_size = request.POST['batch_size']
        tank_num = request.POST['tank_num']
        shiftname = request.POST['shiftname']
        created_by = request.POST['created_by']
        plant_name = request.POST['plant_name']

        get_chemical = Chemical.objects.filter(Brand_Name=brand_name)[0]
        #get_chemical.Raw_Materials = ast.literal_eval(get_chemical.Raw_Materials)
        get_chemical.Technicals= ast.literal_eval(get_chemical.Technicals)

        count = Batch_Card.objects.filter(Brand_Name=brand_name).count()
        batchcardno = get_chemical.Brand_No+str(date.year % 10) + str(date.month).zfill(2) + str(count + 1).zfill(3)

        thbatch_size = int(batch_size) / get_chemical.SPGR
        thbatch_size = round(thbatch_size, 2)

        exp_date= str((date-datetime.timedelta(1)) + relativedelta(years=get_chemical.expiry))

        for i in get_chemical.Technicals:
            if get_chemical.Base_Calc == "Batch_Size":
                theo_qty = float(batch_size) * i["Target_Base"]
                theo_qty = round(theo_qty, 2)
                i.update({"theo_qty": theo_qty})
            if get_chemical.Base_Calc == "THBatch_Size":
                theo_qty = float(thbatch_size) * i["Target_Base"]
                theo_qty = round(theo_qty, 2)
                i.update({"theo_qty": theo_qty})


        Batch_Card.objects.create(
            ShiftName=shiftname,
            Created_Date=date,
            Product_Category=product_category,
            BatchCardNo=batchcardno,
            Brand_Name=brand_name,
            Brand_No=get_chemical.Brand_No,
            Batch_Size=batch_size,
            Plant_Name = plant_name,
            THBatch_Size= thbatch_size,
            Tank_Num=tank_num,
            SAP_Code=get_chemical.SAP_Code,
            SPGR=get_chemical.SPGR,
            Chemical_name=get_chemical.Chemical_name,
            Base_Calc=get_chemical.Base_Calc,
            Created_By=created_by,
            MFG_Date=date,
            Expiry=get_chemical.expiry,
            Expiry_Date=exp_date,
            Technicals=get_chemical.Technicals,
            Raw_Materials=get_chemical.Raw_Materials,
        )

        get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)
        get_batchcard.Raw_Materials = ast.literal_eval(get_batchcard.Raw_Materials)
        get_batchcard.Technicals = ast.literal_eval(get_batchcard.Technicals)

        return render(request, 'newbatchcard.html',{"data":data,"display_list":get_batchcard,'notifications':notifications,'user_permissions':user_permissions})

    if request.method == 'POST' and 'form2' in request.POST or 'form3' in request.POST:
        batchcardno = request.POST["batchcardno"]
        get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)
        get_batchcard.Raw_Materials = ast.literal_eval(get_batchcard.Raw_Materials)
        get_batchcard.Technicals = ast.literal_eval(get_batchcard.Technicals)

        purity = request.POST.getlist('purity[]')

        supplier_name = request.POST.getlist('supplier_name')
        supplier_batch = request.POST.getlist('supplier_batch')
        if "Target_Base" in request.POST:
            Target_Base = request.POST['Target_Base']
        remark = request.POST['remark']
        theo_qty = request.POST.getlist('theo_qty[]')
        chemicals_select = request.POST.getlist('Chemicals')
        #print("*************")
        #print("Selected Chemicals",chemicals_select)
        if "dual_percent" in request.POST:
            #print("Dual percent chemical")
            dual_percent = request.POST.getlist('dual_percent')

        else:
            #print("Not a dual percent chemical")
            dual_percent = 0
        count = len(get_batchcard.Technicals)
        for i in range(0, count):
            get_batchcard.Technicals[i].update(
                {
                    "purity": purity[i],
                    "supplier_name": supplier_name[i],
                    "supplier_batch": supplier_batch[i],
                    "theo_qty": theo_qty[i],
                    "actual_qty": 0
                }
            )
        list_one = []
        list_two = []
        list_three = []
        tth = 0
        trm = 0
        for item in get_batchcard.Raw_Materials:
            if item["Name"] in chemicals_select:
                if item["Type"] == "Solvent":
                    list_three.append(item)
                    #print("Solvent Chemicals")
                    #print(list_three)
                elif item["Type"] == "Dual":
                    list_two.append(item)
                    # print("Dual Chemicals")
                    # print(list_two)
                else:
                    list_one.append(item)
                    #print("Fixed Chemicals")
                    #print(list_one)
        for item in list_one:
            if get_batchcard.Base_Calc == "Batch_Size":
                theo_qty = item["Target_Base"] * get_batchcard.Batch_Size / 100
            if get_batchcard.Base_Calc == "THBatch_Size":
                theo_qty = item["Target_Base"] * get_batchcard.THBatch_Size / 100
            theo_qty = round(theo_qty,2)
            item.update({
                "theo_qty": theo_qty,
                "actual_qty": 0
            })
            #print(item["Name"],item["theo_qty"])

        for item in range(0,len(list_two)):
            if get_batchcard.Base_Calc == "Batch_Size":
                if dual_percent != 0:
                    combined_percentage = (list_two[item]["Target_Base"] * get_batchcard.Batch_Size / 100)
                    theo_qty = (list_two[item]["Target_Base"] * get_batchcard.Batch_Size / 100) * \
                               int(dual_percent[item]) / 100
                    #print("combined percentage", combined_percentage)
                    #print("theo_qty",theo_qty)

            if get_batchcard.Base_Calc == "THBatch_Size":
                if dual_percent != 0:
                    combined_percentage = (list_two[item]["Target_Base"] * get_batchcard.THBatch_Size / 100)
                    theo_qty = (list_two[item]["Target_Base"] * get_batchcard.THBatch_Size / 100) * \
                               int(dual_percent[item]) / 100
                    #print("combined percentage", combined_percentage)
                    #print("theo_qty", theo_qty)

            theo_qty = round(theo_qty, 2)
            list_two[item].update({
                "theo_qty": theo_qty,
                "dual_percent": dual_percent[item],
                "actual_qty": 0
            })
            #print(list_two[item]["Name"], list_two[item]["theo_qty"])
        for item in list_three:
            for i in get_batchcard.Technicals:
                if "theo_qty" in i:
                    tth = float(i["theo_qty"]) + tth
            for i in get_batchcard.Raw_Materials:
                if "theo_qty" in i:
                    trm = float(i["theo_qty"]) + trm
            if get_batchcard.Base_Calc == "Batch_Size":
                theo_qty = get_batchcard.Batch_Size - (tth+trm)
            if get_batchcard.Base_Calc == "THBatch_Size":
                theo_qty = get_batchcard.THBatch_Size - (tth+trm)
            theo_qty = round(theo_qty, 2)
            item.update({
                "theo_qty": theo_qty,
                "actual_qty": 0
            })
            #print(item["Name"], item["theo_qty"])
        get_batchcard.Remark = remark
        get_batchcard.save()

        if "form2" in request.POST:
            print("New Batch Card Created Noti")
            create = ["create", get_batchcard.Created_By, "New Batch Card Created",get_batchcard.BatchCardNo,"edit_batchcard"]
            notification("formulation_shiftincharge", create)
            notification("formulation_lineincharge", create)
        return redirect(batchcard)

    return render(request, 'newbatchcard.html',{"data":data,'notifications':notifications,'user_permissions':user_permissions})


@login_required(login_url='login')
def editbatchcard(request,batchcardno):
    user_permissions = role_checker(request, "edit_batchcard")[0]
    notifications = notification(role_checker(request, "edit_batchcard")[1],"view")

    if user_permissions is False:
        return redirect(no_access)

    get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)

    if request.method == "GET":
        batchcard_list = Batch_Card.objects.get(BatchCardNo = batchcardno)
        batchcard_list.Raw_Materials = ast.literal_eval(batchcard_list.Raw_Materials)
        batchcard_list.Technicals = ast.literal_eval(batchcard_list.Technicals)
        return render(request, 'editbatchcard.html',{"display_list":batchcard_list,"user_permissions":user_permissions,"notifications":notifications})

    if request.method == "POST" and "Approve" in request.POST:
        print("Approvallll")
        get_batchcard.BatchCard_Approval = "InProgress"
        get_batchcard.save()
        ebc_list = ["create", get_batchcard.Created_By, "Batchcard Approved", get_batchcard.BatchCardNo, "view_batchcard"]
        notifications = notification("formulation_operator", ebc_list)
        #return redirect(batchcard)

    if request.method == "POST" and "Reject" in request.POST:
        print("Reject")
        get_batchcard.BatchCard_Approval = "Pending"
        get_batchcard.save()
        ebc_list = ["create", get_batchcard.Created_By, "Batchcard Rejected", get_batchcard.BatchCardNo, "edit_batchcard"]
        notifications = notification("formulation_operator", ebc_list)
        return redirect(batchcard)

    if request.method == "POST" or "submit" in request.POST or 'form3' in request.POST or "Approve" in request.POST:
        total =0
        t = 0
        print("IN THE SUBMIT")

        batchcardno = request.POST['batchcarno']
        batch_size = request.POST['batch_size']
        TechnicalName = request.POST.getlist('TechnicalName')
        purity = request.POST.getlist('purity[]')
        theo_qty = request.POST.getlist('theo_qty[]')
        supplier_name = request.POST.getlist('supplier_name')
        supplier_batch = request.POST.getlist('supplier_batch')
        dual_percent = request.POST.getlist('dual_percent')
        remark = request.POST['remark']
        chemicals_select = request.POST.getlist('Chemicals')

        get_batchcard.Batch_Size = int(batch_size)
        get_batchcard.Raw_Materials = ast.literal_eval(get_batchcard.Raw_Materials)
        get_batchcard.Technicals = ast.literal_eval(get_batchcard.Technicals)

        for i in range(0,len(get_batchcard.Technicals)):
            if get_batchcard.Technicals[i]["Name"] == TechnicalName[i]:
                get_batchcard.Technicals[i]["theo_qty"] = theo_qty[i]
                get_batchcard.Technicals[i]["purity"] = purity[i]
                get_batchcard.Technicals[i]["supplier_name"] = supplier_name[i]
                get_batchcard.Technicals[i]["supplier_batch"] = supplier_batch[i]
        list_one = []
        list_two = []
        list_three = []
        t = 0

        for item in get_batchcard.Raw_Materials:
            if item["Name"] not in chemicals_select:
                if "theo_qty" in item:
                    print(item.pop("theo_qty"))

        for item in get_batchcard.Raw_Materials:
            if item["Name"] in chemicals_select:
                if item["Type"] == "Solvent":
                    list_three.append(item)
                elif item["Type"] == "Dual":
                    list_two.append(item)
                else:
                    list_one.append(item)

        for item in list_one:
            if get_batchcard.Base_Calc == "Batch_Size":
                theo_qty = item["Target_Base"] * int(get_batchcard.Batch_Size) / 100
            if get_batchcard.Base_Calc == "THBatch_Size":
                theo_qty = item["Target_Base"] * int(get_batchcard.THBatch_Size) / 100
            item.update({
                "theo_qty": theo_qty
            })

        for item in range(0, len(list_two)):
            if get_batchcard.Base_Calc == "Batch_Size":
                if dual_percent != 0:
                    combined_percentage = (list_two[item]["Target_Base"] * get_batchcard.Batch_Size / 100)
                    theo_qty = (list_two[item]["Target_Base"] * get_batchcard.Batch_Size / 100) * \
                               int(dual_percent[item]) / 100
            if get_batchcard.Base_Calc == "THBatch_Size":
                theo_qty = (list_two[item]["Target_Base"] * get_batchcard.THBatch_Size / 100) * \
                           int(dual_percent[item]) / 100
            theo_qty = round(theo_qty, 2)
            list_two[item].update({
                "theo_qty": theo_qty,
                "dual_percent": dual_percent[item]
            })
        for item in list_three:
            for i in get_batchcard.Technicals:
                if "theo_qty" in i:
                    t = float(i["theo_qty"]) + t
            # print("Total Technicals",t)
            for i in get_batchcard.Raw_Materials:
                if "theo_qty" in i:
                    t = float(i["theo_qty"]) + t
            # print("Total Raw Materials", t)
            if get_batchcard.Base_Calc == "Batch_Size":
                theo_qty = int(get_batchcard.Batch_Size) - t
            if get_batchcard.Base_Calc == "THBatch_Size":
                theo_qty = get_batchcard.THBatch_Size - t
            # print("Theo qty",theo_qty)
            theo_qty = round(theo_qty, 2)
            item.update({
                "theo_qty": theo_qty
            })
        get_batchcard.Remark = remark
        get_batchcard.save()
        return redirect(batchcard)
    return render(request, 'editbatchcard.html', {'user_permissions': user_permissions, 'notifications': notifications})


@login_required(login_url='login')
def viewbatchcard(request,batchcardno):
    user_permissions = role_checker(request, "view_batchcard")[0]
    notifications = notification(role_checker(request, "view_batchcard")[1],"view")

    if user_permissions is False:
        return redirect(no_access)

    batchcard_list = Batch_Card.objects.get(BatchCardNo=batchcardno)
    batchcard_list.Raw_Materials = ast.literal_eval(batchcard_list.Raw_Materials)
    batchcard_list.Technicals = ast.literal_eval(batchcard_list.Technicals)
    return render(request, 'viewbatchcard.html',{"display_list":batchcard_list, "user_permissions":user_permissions,"notifications":notifications})


@login_required(login_url='login')
def viewreceipe(request, batchcardno):
    user_permissions = role_checker(request, "view_receipe")[0]
    notifications = notification(role_checker(request, "view_receipe")[1],"view")

    if user_permissions is False:
        return redirect(no_access)

    if request.method == "GET":
        print(batchcardno)
        batchcard_list = Batch_Card.objects.get(BatchCardNo = batchcardno)
        raw_materials = ast.literal_eval(batchcard_list.Raw_Materials)
        print(raw_materials)
        technicals = ast.literal_eval(batchcard_list.Technicals)
        #print(technicals)
        return render(request, 'viewrecipe.html',{"raw_materials":raw_materials,'technicals':technicals,"user_permissions":user_permissions,"notifications":notifications})


@login_required(login_url='login')
def productrecipe(request, batchcardno):
    user_permissions = role_checker(request, "add_view_chemicals")[0]
    notifications = notification(role_checker(request, "add_view_chemicals")[1], "view")

    chemicals = []
    get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)
    sample_list = Sample.objects.all()
    raw_materials = ast.literal_eval(get_batchcard.Raw_Materials)
    technicals = ast.literal_eval(get_batchcard.Technicals)
    sample_data = ast.literal_eval(get_batchcard.Add_Sample)
    chemicals = technicals+raw_materials
    date = datetime.date.today()
    time = datetime.datetime.now().time().replace(microsecond=0)
    date_time={"date":date,"time":time}
    add_chemicals_lists = ast.literal_eval(get_batchcard.Add_Chemical)
    keys = ["ChemcialName","Percentage","QuantityAdded","DateTime","LoadCellStart","LoadCellReading","LoadCellEnd","Operator"]


    #if request.method == "POST":

    if request.method == "POST" and "sample" in request.POST:
        sample_type = request.POST["sample_type"]
        created_date = request.POST["date"]
        created_time = request.POST["time"]
        quantity = request.POST["sample_qty"]
        comments = request.POST["comments"]

        sample_data.append({
            "sample_type":sample_type,
            "created_date":created_date,
            "created_time":created_time,
            "quantity":quantity,
            "comments":comments
        })
        get_batchcard.Add_Sample = sample_data
        get_batchcard.save()

    if request.method =="POST" and "add_chemical" in request.POST:
        chemical = request.POST["chemical"]
        date = request.POST["date"]
        time = request.POST["time"]
        created_by= request.POST["createdby"]
        addqty = 0

        for i in technicals:
            if chemical == i["Name"]:
                print("Technical found")
                if "actual_qty" in i:
                    addqty = request.POST["addqty"]
                    actual_qty = i["actual_qty"]
                    print("actual qty", actual_qty)
                    i["actual_qty"] = int(actual_qty)+int(addqty)
                    print("Updated actual qty in technicals")
                    print(chemical, addqty, i["actual_qty"])
        for i in raw_materials:
            if chemical == i["Name"]:
                print("Raw Material found")
                if "actual_qty" in i:
                    addqty = request.POST["addqty"]
                    actual_qty = i["actual_qty"]
                    print("actual qty",actual_qty)
                    i["actual_qty"] = int(actual_qty) + int(addqty)
                    print("Update actual qty in raw materials")
                    print(chemical, addqty, i["actual_qty"])
        print(chemical, addqty)
        if addqty != 0:
            addlist = {"ChemcialName":chemical, "DateTime":date+time, "QuantityAdded":addqty, "created_by":created_by}
            add_chemicals_lists.append(addlist)
            get_batchcard.Add_Chemical = add_chemicals_lists
            get_batchcard.Raw_Materials = raw_materials
            get_batchcard.Technicals = technicals
            get_batchcard.save()

            print("saved")
        else:
            print("not saved")
        return render(request, 'productrecipe.html',{"chemicals": chemicals, 'get_batchcard': get_batchcard, "date_time":date_time,"lists":add_chemicals_lists,"keys":keys,"sample_list":sample_list,"sample_data":sample_data,"user_permissions":user_permissions,"notifications":notifications})
    return render(request, 'productrecipe.html', {"chemicals": chemicals, 'get_batchcard': get_batchcard,"date_time":date_time,"lists":add_chemicals_lists,"keys":keys,"sample_list":sample_list,"sample_data":sample_data,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def viewchemical(request, batchcardno):
    user_permissions = role_checker(request, "add_view_chemicals")[0]
    notifications = notification(role_checker(request, "add_view_chemicals")[1], "view")
    get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)
    sample_list = Sample.objects.all()
    add_chemicals_lists = ast.literal_eval(get_batchcard.Add_Chemical)
    raw_materials = ast.literal_eval(get_batchcard.Raw_Materials)
    technicals = ast.literal_eval(get_batchcard.Technicals)
    sample_data = ast.literal_eval(get_batchcard.Add_Sample)
    chemicals = technicals + raw_materials
    return render(request, 'viewchemical.html',
                  {"chemicals": chemicals, 'get_batchcard': get_batchcard,
                   "lists": add_chemicals_lists, "sample_list": sample_list, "sample_data": sample_data,
                   "user_permissions": user_permissions, "notifications": notifications})


@login_required(login_url='login')
def completebatchcard(request, batchcardno):
    get_batchcard = Batch_Card.objects.get(BatchCardNo=batchcardno)
    if request.method == "GET" and "submit" in request.GET:
        ebc_list = ["create", get_batchcard.Created_By, "Add Chemicals Complete", get_batchcard.BatchCardNo,
                    "viewchemical"]
        notifications = notification("formulation_shiftincharge", ebc_list)
        print("batchcard submitteed")

    if request.method == "GET" and "complete" in request.GET:
        get_batchcard.BatchCard_Approval = "Completed"
        get_batchcard.save()
        ebc_list = ["create", get_batchcard.Created_By, "Batchcard Completed", get_batchcard.BatchCardNo, "view_batchcard"]
        notification("formulation_operator", ebc_list)
        print("batchcard completed")

    return redirect(batchcard)


def create_user(request):
    print("create_user function")

    if request.method == 'POST':

        form = UserDetailsForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            form.save()
            print("form saved")
            u_n = form.data['Username']
            u_p = form.data['Password']
            User.objects.create_user(username=u_n, password=u_p)
        else:
            print("form not saved not valid")
        '''            
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
        '''
        return redirect('profile')





@login_required(login_url='login')
def profile(request):
    user_permissions = role_checker(request, "profile")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    users = User_Data.objects.all()
    shift_list = Shift.objects.all()
    plant_list= Plant_Detail.objects.all()
    #print(plant_list[0].ContractorDetails)
    plant_list.PlantName = ast.literal_eval(plant_list[0].PlantName)
    plant_list.LineDetails=ast.literal_eval(plant_list[0].LineDetails)

    if request.method=="GET" and "username" in request.GET:

        data = request.GET["username"]
        print("Username reuested",data)
        b = "No Data"
        for item in users:
            if data in item.Username:
                a = item
                #Name,Username,Password,User_Role,Shift,Status,Plant_name,Line_name
                b = {"Username":a.Name,"Password":a.Password,"User_Role":a.User_Role,"Shift":a.Shift,"Status":a.Status,"plant_name":a.plant_name,"line_name":a.line_name}
                print("item password")
                print(a.Username)
                print(a.Name)
                print(a.Password)
                print("data matched")
        print(b)
        return JsonResponse(b)
        #return HttpResponse(json.dumps({"data":a}))
        #return JsonResponse(b)

    return render(request, 'profile.html', {"users_list": users,"shift_list":shift_list, "plant_list":plant_list,"user_permissions":user_permissions,"notifications":notifications})


def ajax_test(request):
    if request.method=="GET":

        data = request.GET["data"]
        print(data)
        if data=="ALFKI":
            a = '{"username":"vivek","password":"vivek@123","shit":"A","line":"FM301"}'
            print("data matched")
        else:
            print("data not matched")
        return HttpResponse(a)
        #return JsonResponse(a)

    if request.method=="POST":
        for key, value in request.POST.items():
            print('Key: %s' % (key))
            print('Value %s' % (value))

    return HttpResponse("NO REQUEST")



@login_required(login_url='login')
def group(request):
    groups = [{"GroupName": "Operator"}, {"GroupName": "Shift Incharge"}, {"GroupName": "Line Incharge"}]
    '''
    if request.method == 'POST':
        username = request.POST['Group']

        batch_cards_one = request.POST['batch_cards_one']
        batch_cards_two = request.POST['batch_cards_two']
        tasks_one = request.POST['tasks_one']
        tasks_two = request.POST['tasks_two']
        maintenance_one = request.POST['maintenance_one']
        maintenance_two = request.POST['maintenance_two']
        sops_one = request.POST['sops_one']
        sops_two = request.POST['sops_two']
        alarms_one = request.POST['alarms_one']
        alarms_two = request.POST['alarms_two']
        profiles_one = request.POST['profiles_one']
        profiles_two = request.POST['profiles_two']
        mp_plan_one = request.POST['mp_plan_one']
        mp_plan_two = request.POST['mp_plan_two']
        prod_plan_one = request.POST['prod_plan_one']
        prod_plan_two = request.POST['prod_plan_two']

        username = request.POST['username']
        password = request.POST['password']
    '''

    for key, value in request.POST.items():
        print('Key: %s' % (key))
        print('Value %s' % (value))

    return render(request, 'profile-group.html', {'groups':groups})

@login_required(login_url='login')
def manpowerplanning(request):
    user_permissions = role_checker(request, "manpower")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)
    manpower_list = ManPower_Detail.objects.all()
    return render(request, 'manpowerplanning.html',{"manpower_list":manpower_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def newmanpowerplanning(request):
    user_permissions = role_checker(request, "manpower")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    today_date = datetime.date.today()
    shift_list = Shift.objects.all()
    plant_data = Plant_Detail.objects.all()
    plant_list = plant_data[0]
    plant_list.PlantName = ast.literal_eval(plant_list.PlantName)
    plant_list.ContractorDetails = ast.literal_eval(plant_list.ContractorDetails)
    plant_list.AllotmentDetails = ast.literal_eval(plant_list.AllotmentDetails)
    #print(plant_list.PlantName[1])


    if request.method == 'POST':
        createddate = request.POST["createddate"]
        shift = request.POST["shift"]
        allotteddate = request.POST["allotteddate"]
        allotment=request.POST["allotment"]
        noofallotment = request.POST["noofallotment"]
        contractor = request.POST["contractor"]
        plant = request.POST["plant"]

        ManPower_Detail.objects.create(
            CreatedDate=createddate,
            AllottedDate = allotteddate,
            shift = shift,
            contractor = contractor,
            allotment = allotment,
            noofalotment = noofallotment,
            plant = plant
        )

        return redirect(manpowerplanning)

    return render(request, 'newmanpowerplanning.html',{"today_date":today_date,"shift_list":shift_list,"plant_list":plant_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def maintenance(request):
    user_permissions = role_checker(request, "maintenance")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    maintenance_list = Maintenance_Detail.objects.all()
    return render(request, 'maintenance.html',{"maintenance_list":maintenance_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def editmaintenance(request,id):
    user_permissions = role_checker(request, "maintenance")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    maintenance_list = Maintenance_Detail.objects.get(id = id)
    if request.method == "POST":
        maintenance_list.status = request.POST["status"]
        maintenance_list.save()

        return redirect(maintenance)
    return render(request, 'editmaintenance.html',{"maintenance_list":maintenance_list,"user_permissions":user_permissions,"notifications":notifications})


@login_required(login_url='login')
def planmaintenance(request):
    user_permissions = role_checker(request, "maintenance")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    today_date = datetime.date.today()
    shift_list = Shift.objects.all()
    plant_data = Plant_Detail.objects.all()
    plant_list = plant_data[0]
    plant_list.PlantName = ast.literal_eval(plant_list.PlantName)
    plant_list.LineDetails = ast.literal_eval(plant_list.LineDetails)
    plant_list.MachineDetails = ast.literal_eval(plant_list.MachineDetails)

    print("usrrr",str(request.user))

    user_details = User_Data.objects.get(Username=str(request.user))
    if request.method == "POST":
        startdatetime = request.POST["startdatetime"]
        maintenancetype = request.POST["maintenancetype"]
        if maintenancetype == "Scheduled":
            status = "Pending"
        else:
            status = "NA"
        plant = request.POST["plant"]
        line = request.POST["line"]
        machine = request.POST["machine"]
        equipment = request.POST["equipment"]
        part = request.POST["part"]
        enddatetime = request.POST["enddatetime"]
        reason = request.POST["reason"]
        created_by = str(request.user)

        Maintenance_Detail.objects.create(
            startdatetime=startdatetime,
            maintenancetype=maintenancetype,
            status=status,
            plant=plant,
            line=line,
            machine=machine,
            equipment=equipment,
            part=part,
            enddatetime=enddatetime,
            reason=reason,
            created_by = created_by
        )
        #id = CreateTask.objects.all().last().id
        #print("id", id)
        create = ["create", created_by, "New Maintenance Created", id, "editmaintenance"]
        if user_details.process == "Formulation" and user_details.Username == "operator":
            notification("formulation_shiftincharge", create)
            notification("formulation_lineincharge", create)
        if user_details.process == "Packaging" and user_details.Username == "operator":
            notification("packaging_shiftincharge", create)
            notification("packaging_lineincharge", create)
        return redirect(maintenance)
    return render(request, 'planmaintenance.html',{"today_date":today_date,"shift_list":shift_list,"plant_list":plant_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def deletemaintenance(request, id):
    Maintenance_Detail.objects.filter(id = id).delete()
    print(id)
    print("Delete")
    return redirect(maintenance)

@login_required(login_url='login')
def reports(request):
    user_permissions = role_checker(request, "reports")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)
    return render(request, 'reports.html',{"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def view_sop(request):
    user_permissions = role_checker(request, "sop")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    sop_list = SOP.objects.all()
    print(sop_list)
    return render(request, 'view_sop.html', {'sop_list':sop_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def create_sop(request):
    user_permissions = role_checker(request, "sop")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    date=datetime.date.today()
    shift_list=Shift.objects.all()

    if request.method == 'POST' and request.FILES["file"]:
        created_date=request.POST["date"]
        sop_name = request.POST["sop_name"]
        created_by = request.POST["created_by"]
        sop_category = request.POST["sop_category"]
        file = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        comment = request.POST["comment"]
        create = SOP.objects.create(
            created_date = created_date,
            sop_name=sop_name,
            created_by=created_by,
            sop_category=sop_category,
            file=file,
            comment=comment)
        create.save()
        print("CREATED SOP")
        return redirect(view_sop)
    return render(request, 'create_sop.html',{"date":date,"shift_list":shift_list,"notifications":notifications,"user_permissions":user_permissions})


@login_required(login_url='login')
def detail_sop(request,id):
    user_permissions = role_checker(request, "sop")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    sop_list = SOP.objects.get(id=id)

    return render(request, 'detail_sop.html',{"sop_list":sop_list,"notifications":notifications, "user_permissions":user_permissions})

@login_required(login_url='login')
def task(request):
    user_permissions = role_checker(request, "task")[0]
    notifications = notification(role_checker(request, "task")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    tasks_data = CreateTask.objects.all()
    #print(tasks_data[1].id)
    return render(request, 'task.html',{"tasks_data":tasks_data,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def edit_task(request, id):

    user_permissions = role_checker(request, "batchcard")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    task_data = CreateTask.objects.get(id=id)
    if request.method == "POST":
        today_date = datetime.date.today()
        status = request.POST["status"]
        comment = request.POST["comment"]
        task_data.status = status
        task_data.comment = comment
        task_data.completed_date = today_date
        task_data.save()

        return redirect(task)
    return render(request, 'edit_task.html',{"task_data":task_data,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def create_task(request):
    user_permissions = role_checker(request, "create_task")[0]
    notifications = notification(role_checker(request, "create_task")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    shift_list = Shift.objects.all()
    today_date = datetime.date.today()
    tasks_list = Tasks_list.objects.all()
    user_details = User_Data.objects.get(Username=str(request.user))
    print("usrrrrr",user_details.process)
    user_list=[]
    print(request.user)
    if str(request.user) == "admin":
        user_list = ["Line Incharge","Shift Incharge","Operator"]
    if str(request.user) == "shiftincharge" or str(request.user) == "p_shiftincharge":
        user_list = ["Operator"]
    if str(request.user) == "lineincharge" or str(request.user) == "p_lineincharge":
        user_list = ["Shift Incharge","Operator"]
    if request.method == "POST":
        #shift = request.POST["shift"]
        created_date = request.POST["date"]
        task_selected = request.POST["task_selected"]
        assigned = request.POST["assigned"]
        activity = request.POST["Activity"]
        comment = request.POST["comment"]
        created_by = str(request.user)

        CreateTask.objects.create(
            #shift = shift,
            task=task_selected,
            activity = activity,
            assigned = assigned,
            comment = comment,
            created_date = created_date,
            created_by = created_by,
        )
        id= CreateTask.objects.all().last().id
        print("id",id)
        create = ["create", created_by, "New Task Assigned", id,"edit_task"]
        if user_details.process == "Formulation" and assigned == "Operator":
            notification("formulation_operator", create)
        if user_details.process == "Formulation" and assigned == "Shift Incharge":
            notification("formulation_shiftincharge", create)
        if user_details.process == "Packaging" and assigned == "Operator":
            notification("packaging_operator", create)
        if user_details.process == "Packaging" and assigned == "Shift Incharge":
            notification("packaging_shiftincharge", create)
        return redirect(task)

    return render(request, 'create_task.html',{"user_list":user_list,"shift_list":shift_list, "date":today_date, "tasks_list":tasks_list,"user_permissions":user_permissions,"notifications":notifications})

@login_required(login_url='login')
def alerts(request):
    return render(request, 'alerts.html')





'''
newbatchcard view fn code

    for list in Chemical.objects.all():
        chemical = {
            "Brand_Name": list.Brand_Name,
            "Brand_No": list.Brand_No,
            "SAP_Code": list.SAP_Code,
            "SPGR":list.SPGR,
            "Chemical_name": list.Chemical_name,
            "Raw_Materials": ast.literal_eval(list.Raw_Materials),
            "Technicals": ast.literal_eval(list.Technicals),
            "Add_Chemical": [],
            "Add_Sample":[],
            "product_category": list.product_category,
            "expiry": list.expiry
        }
        chemical_list.append(chemical)

    

    

        for i in data["Chemicals"]:
            if brand_name == i["Brand_Name"]:
                display_list = i
                thbatch_size = int(batch_size)/display_list["SPGR"]
                print(type(display_list["SPGR"]), display_list["SPGR"])
                thbatch_size = round(thbatch_size, 2)
                display_list.update(
                    {"batchcardno": display_list["Brand_No"] + batchcardno,
                     "batch_size": int(batch_size),
                     "date": str(date),
                     "mfg_date": str(date),
                     "exp_date": str(date + relativedelta(years=display_list["expiry"])),
                     "tank_num": tank_num,
                     "thbatch_size": thbatch_size,
                     "actual_qty":0,
                     "load_cell":0,
                     "shiftname":shiftname
                     }
                )

        for i in display_list["Technicals"]:
            theo_qty = float(batch_size) * i["Target_Base"]
            theo_qty = round(theo_qty, 2)
            i.update({"theo_qty": theo_qty})

    if request.method == 'POST' and 'form2' in request.POST:
        print("In form 2")

        purity = request.POST.getlist('purity[]')

        supplier_name = request.POST.getlist('supplier_name')
        supplier_batch = request.POST.getlist('supplier_batch')
        Target_Base = request.POST['Target_Base']
        remark = request.POST['remark']
        theo_qty = request.POST.getlist('theo_qty[]')
        chemicals_select = request.POST.getlist('Chemicals')
        count = len(display_list["Technicals"])

        for i in range(0,count):
            display_list["Technicals"][i].update(
                {
                    "purity": purity[i],
                    "supplier_name": supplier_name[i],
                    "supplier_batch": supplier_batch[i],
                    "theo_qty": theo_qty[i],
                    "actual_qty":0
                }
            )
        count = len(chemicals_select)
        total = 0
        t = 0
        for i in range(0, count):
            if chemicals_select[i] != 'NA':
                for j in range(0, len(display_list["Raw_Materials"])):
                    if display_list["Raw_Materials"][j]["Name"] == chemicals_select[i]:
                        if display_list["Raw_Materials"][j]["Target_Base"] == 0:
                            for i in display_list["Technicals"]:
                                if "theo_qty" in i:
                                    t = float(i["theo_qty"]) + t
                                    #print(t)
                                    #print("t in Technicals")
                            for i in display_list["Raw_Materials"]:
                                if "theo_qty" in i:
                                    t = float(i["theo_qty"]) + t
                                    #print(t)
                                    #print("t in Raw_Materials")
                            theo_qty = display_list["batch_size"]-(t)
                            theo_qty = round(theo_qty)
                            #print("total_qty", theo_qty)
                            display_list["Raw_Materials"][j].update(
                                {
                                    "theo_qty": theo_qty
                                })
                            #print("Solvent QTYYYYYYYYYYYY")
                            #print(display_list["Raw_Materials"][j])
                        else:
                            theo_qty = display_list["Raw_Materials"][j]["Target_Base"] * display_list[
                                "batch_size"] / 100
                            theo_qty =round(theo_qty,2)
                        display_list["Raw_Materials"][j].update(
                            {
                                "theo_qty": theo_qty,
                                "actual_qty":0
                            }
                        )
                        total = total + theo_qty

        display_list.update({"remark": remark})
        #print("display_list")
        #print(display_list)

        Batch_Card.objects.create(
            BatchCardNo=display_list["batchcardno"],
            Brand_Name = display_list["Brand_Name"],
            Brand_No = display_list["Brand_No"],
            Batch_Size = display_list["batch_size"],
            THBatch_Size = display_list["thbatch_size"],
            ShiftName = display_list["shiftname"],
            SAP_Code = display_list["SAP_Code"],
            SPGR = display_list["SPGR"],
            Chemical_name = display_list["Chemical_name"],
            Product_Category = display_list["product_category"],
            Date = display_list["date"],
            MFG_Date = display_list["mfg_date"],
            Expiry = display_list["expiry"],
            Expiry_Date = display_list["exp_date"],
            Tank_Num = display_list["tank_num"],
            Remark = display_list["remark"],
            Technicals = display_list["Technicals"],
            Raw_Materials = display_list["Raw_Materials"],
            Add_Chemical=display_list["Add_Chemical"],
        )
        return redirect(batchcard)
'''


'''

editbatchcard view fn
        for i in range(0,len(chemicals_select)):
            for j in range(0,len(raw_materials)):
                if chemicals_select[i] == raw_materials[j]["Name"]:
                    print("SELECTED CHEMICALS")
                    print(chemicals_select[i])
                    if raw_materials[j]["Target_Base"] == 0:
                        for k in range(0,len(technicals)):
                            total = total+float(technicals[k]["theo_qty"])
                        for l in range(0,len(raw_materials)):
                            if "theo_qty" in raw_materials:
                                total = total+float(raw_materials[l]["theo_qty"])
                        c_theo_qty = int(batch_size) - (total+t)
                        raw_materials[j].update({"theo_qty": c_theo_qty})
                    else:
                        c_theo_qty = raw_materials[j]["Target_Base"]*int(batch_size)/100
                        raw_materials[j].update({"theo_qty": c_theo_qty})
                        print("UPDATED RAW MATERIALS")
                        print(raw_materials[j])
                        t = t+c_theo_qty
        for a in range(0, len(raw_materials)):
            for b in range(0, len(chemicals_select)):
                if chemicals_select[b] != raw_materials[a]["Name"]:
                    print("REMOVED CHEMICALS")
                    print(raw_materials[a])
                    print(chemicals_select[b])
'''

'''
                    if "theo_qty" in raw_materials[j]:
                        raw_materials[j].pop("theo_qty")
                    '''


def mssql(ProductName, BatchCardNumber, PackageCardNumber, CreatedBy, PackSize, ProductionCount, ShiftName, shift_starttime, shift_endtime, LineNo, Units_Box, bpm):
    conn = pyodbc.connect(
        'DRIVER={SQL Server};;SERVER=192.168.232.243,1433;DATABASE=Project;UID=adama-db;PWD=Adama$QL22')
    cursor = conn.cursor()

    query0 = "select * from BatchDetails"
    cursor.execute(query0)
    result = cursor.fetchall()
    #print("mssql query result",result)

    if len(result) == 0:
        print("Table Empty")
        cursor.execute(
            "insert into BatchDetails ([ProductName], [BatchCardNumber], [PackageCardNumber], [CreatedBy], [PackSize], [ProductionCount], [ShiftName], [LineNo], [ShiftStartTime], [ShiftEndTime], [Units_Box], [bpm]) values (?,?,?,?,?,?,?,?,?,?,?,?)",
            ProductName, BatchCardNumber, PackageCardNumber, CreatedBy, PackSize, ProductionCount, ShiftName, LineNo,shift_starttime, shift_endtime, Units_Box, bpm)
        conn.commit()

    else:
        print("Table not Empty")
        cursor.execute("""select * from BatchDetails where [LineNo] = ? """, LineNo)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute(
                "insert into BatchDetails ([ProductName], [BatchCardNumber], [PackageCardNumber], [CreatedBy], [PackSize], [ProductionCount], [ShiftName], [LineNo], [ShiftStartTime], [ShiftEndTime], [Units_Box], [bpm]) values (?,?,?,?,?,?,?,?,?,?,?,?)",
                ProductName, BatchCardNumber, PackageCardNumber, CreatedBy, PackSize, ProductionCount, ShiftName,
                LineNo,shift_starttime, shift_endtime, Units_Box, bpm)
            conn.commit()
            print("new lineno inserted")
        else:
            cursor.execute(
                "UPDATE BatchDetails SET [ProductName]= ?, [BatchCardNumber]= ?, [PackageCardNumber]= ?, [CreatedBy]= ?, [PackSize]= ?, [ProductionCount]= ?, [ShiftName]= ?, [LineNo]= ?, [ShiftStartTime]=?, [ShiftEndTime]=?, [Units_Box]= ?, [bpm]= ? WHERE [LineNo] = ?",
                ProductName, BatchCardNumber, PackageCardNumber, CreatedBy, PackSize, ProductionCount, ShiftName,
                LineNo,shift_starttime, shift_endtime, Units_Box, bpm, LineNo)
            conn.commit()
            print("existing lineno updated")
    conn.close()






@login_required(login_url='login')
def group_sec(request):
    return render(request, 'group_sec.html')

@login_required(login_url='login')
def user_register(request):
    return render(request, 'register.html')

@login_required(login_url='login')
def sample(request):
    for key, value in request.POST.items():
        print('Key: %s' % (key))
        print('Value %s' % (value))
    return render(request, 'sample.html')



@register.filter
def get_range(value):
    return range(value)


@login_required(login_url='login')
def packaging(request):
    user_permissions = role_checker(request, "view_package")[0]
    notifications = notification(role_checker(request, "create_batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    batchcard_list = Batch_Card.objects.filter(BatchCard_Approval="Completed")
    # packagecard_list = PackageCard.objects.all()
    packagecard_list = PackageCard.objects.all().order_by('PackageCardNo')
    print(packagecard_list[0])

    return render(request, 'packaging.html',{"batchcard_list":batchcard_list,"packagecard_list":packagecard_list,"user_permissions":user_permissions,"notifications":notifications})


@login_required(login_url='login')
def newplanpackaging(request, created_date=None):
    #updating_table=PackageCard.objects.filter(Created_Date='April 27, 2023').update(PackageCardApproval='' , PackageCardStatus='')

    user_permissions = role_checker(request, "create_package")[0]
    notifications = notification(role_checker(request, "create_batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    #batchcard_list = Batch_Card.objects.filter(BatchCard_Approval="Completed")
    product_list = Chemical.objects.values("Brand_Name")
    plant_list = ast.literal_eval(Plant_Detail.objects.values("PlantName")[0]["PlantName"])
    shift_list = Shift.objects.all()
    line_list = ast.literal_eval(Plant_Detail.objects.values("LineDetails")[0]["LineDetails"])
    today_date = datetime.date.today()
    PackageCardNo = 0


    for key, value in request.POST.items():
        print('Key: %s' % (key))
        print('Value %s' % (value))

    if request.method=="POST" and "newplan" in request.POST:
        print("newplanpackaging,newplanpackaging")
        batchcardno = request.POST["batchcardno"]
        shift = request.POST["shift"]
        line = request.POST["line"]
        created_date = request.POST["created_date"]
        created_by = request.POST["created_by"]
        plant_name = request.POST["plantname"]
        product_name = request.POST["productname"]

        count = PackageCard.objects.all().count()
        PackageCardNo = str(today_date.year % 10) + str(today_date.month) + str(count + 1).zfill(3)
        # get_batchcard = Batch_Card.objects.filter(BatchCardNo=batchcardno)
        spgr = "1"
        # plant_name = get_batchcard[0].Plant_Name

        PackageCard.objects.create(
            BatchCardNo = batchcardno,
            PackageCardNo = PackageCardNo,
            ShiftName = shift,
            LineName =line,
            Created_Date=created_date,
            SPGR=spgr,
            Chemical_name=product_name,
            Created_By = created_by,
            Plant_Name = plant_name,
        )

        print("package card created")
        get_packagecard = PackageCard.objects.filter(PackageCardNo=PackageCardNo)

        print("New Package Card Created Noti")
        create = ["create", get_packagecard[0].Created_By, "New Package Card Created", get_packagecard[0].PackageCardNo,
                  "editpackaging"]
        notification("packaging_shiftincharge", create)
        notification("packaging_lineincharge", create)


        return render(request, 'newplanpackaging.html',
                      {"plant_list":plant_list,"product_list":product_list, "shift_list": shift_list, "line_list": line_list,
                       "today_date": today_date,"get_packagecard":get_packagecard[0]})

    if request.method=="POST" and "createplan" in request.POST:

        if request.method=="POST":
            batchcardno = request.POST["batchcardno"]
            packagecardno = request.POST["packagecardno"]
            packsize = request.POST["packsize"]
            netwt=request.POST["netwt"]
            # box_type = request.POST["box_type"]
            box_type = ""

            units = request.POST["units"]
            # productioncount = request.POST["productioncount"]
            productioncount = "0"
            avgwt=request.POST["avgwt"]
            grosswt=request.POST["grosswt"]
            plugwt=request.POST["plugwt"]
            stdwt=request.POST["stdwt"]
            minstdqtypercent=request.POST["minstdqtypercent"]
            minstdqty=request.POST["minstdqty"]
            maxstdqtypercent=request.POST["maxstdqtypercent"]
            maxstdqty=request.POST["maxstdqty"]
            remark=request.POST["remark"]
            instruction=request.POST["instruction"]
            bpm = request.POST["bpm"]

            get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)

            get_packagecard.Packsize = int(packsize)
            get_packagecard.MaterialNetWt = netwt
            get_packagecard.BoxType = box_type
            get_packagecard.Units_Box = int(units)
            get_packagecard.ProductionCount = int(productioncount)
            get_packagecard.ContainerWt = avgwt
            get_packagecard.GrossWt = grosswt
            get_packagecard.CapAvgWt = plugwt
            get_packagecard.StdWt = stdwt
            get_packagecard.MinPercent = minstdqtypercent
            get_packagecard.MinStdWt = minstdqty
            get_packagecard.MacPercent = maxstdqtypercent
            get_packagecard.MaxStdWt = maxstdqty
            get_packagecard.Remark =remark
            get_packagecard.Instructions =instruction
            get_packagecard.bpm = bpm
            get_packagecard.save()
        return redirect(packaging)

    json = {
        "plant_list": plant_list, "product_list": product_list, "shift_list": shift_list, "line_list": line_list,
        "today_date": today_date, "notifications": notifications, "user_permissions": user_permissions,
        "plant_details":
            {
                "Herbicide1": ["FM301","FM302","FM303","FM304","FM305","FM306","FM401","FM402"],
                "Insecticide1": ["FM101","FM102","FM103","FM104","FM105"],
                "Insecticide2": ["FM701","FM702","FM703","FM801-A","FM801-B","FM801-C","FM801-D","FM404"],
                "WDG": ["FM1001"],
                "NIMITZ": ["FM901"]
            },
        "product_details":
            {
                "Herbicide1": ["AGIL","AIRETH","DEKEL","DIUREX","EVENSO","FLITZER","GALIGAN EC","GALIL","MAINBOOST","MAINSPREED","NARKIS","PADIWIX","PARANEX SL","PRETIGAN EC","ROWLOCK","SHAKED","TAMAR","WEEDBLOCK","WIDIGO","ZETROLA","LIVYATAN"],
                "Insecticide1": ["AAKOFOS 48 EC","ABANEX","ACEMAIN SP","ACETA STAR","ADAPHON","AGADI SC","AGAS","ALMAGOR","APROPO","ATENZA","BARAZIDE","BLASIL","BRENTZ","BUMPER","COHIGAN STRONG","COSAYR","CUSTODIA","FLAMBERGE","IMPERIAL","ISOMAIN","KOHAV","LAMDEX EC","LAMDEX SUPER EC","LAPIDOS","MAINEX EC","MAINEX SC","MAINSTAR","MASTERCOP","MASTERCOP","MISHMISH","NIMITZ","NIMROD","NIRIA","OLANDER","ORIUS","PEDESTAL EC","PLETHORA","PREMAIN","PREMAIN STRONG","PREMAIN SUPER EC","PROFIGAN PLUS EC","SEIZER","SHAMIR","SHORESH","SIGALIT","STARTUP","SUCKGAN WG","TAKAF","TAPUZ","TARBUT","YAFFIT","ZAMIR","ZOHAR","TRIGUS","TORMOS","ANOLIK"]
            }
        }
    return render(request, 'newplanpackaging.html',json)


@login_required(login_url='login')
def directpackaging(request):

    return render(request, 'directpackaging.html')


@login_required(login_url='login')
def newpackaging(request, packagecardno):
    user_permissions = role_checker(request, "batchcard")[0]
    notifications = notification(role_checker(request, "batchcard")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
    if request.method=="POST":
        machine_speed = request.POST["machine_speed"]
        nozzle_one = request.POST["nozzle_one"]
        nozzle_two = request.POST["nozzle_two"]
        nozzle_three = request.POST["nozzle_three"]
        nozzle_four = request.POST["nozzle_four"]
        nozzle_five = request.POST["nozzle_five"]
        nozzle_six = request.POST["nozzle_six"]

        get_packagecard.machine_speed=machine_speed
        get_packagecard.nozzle_one=nozzle_one
        get_packagecard.nozzle_two=nozzle_two
        get_packagecard.nozzle_three=nozzle_three
        get_packagecard.nozzle_four=nozzle_four
        get_packagecard.nozzle_five=nozzle_five
        get_packagecard.nozzle_six=nozzle_six
        get_packagecard.save()

        return redirect(packaging)
    return render(request, 'newpackaging.html',{"get_packagecard":get_packagecard, "notifications":notifications, "user_permissions":user_permissions})


@login_required(login_url='login')
def editpackaging(request, packagecardno):

    user_permissions = role_checker(request, "edit_package")[0]
    notifications = notification(role_checker(request, "edit_package")[1], "view")

    if user_permissions is False:
        return redirect(no_access)

    get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
    print("requesttttttt", request.POST)
    if request.method=="POST" and 'print' in request.POST:
        print("print")
        pdf = html_to_pdf('editpackaging.html')
        return HttpResponse(pdf, content_type='application/pdf')

    if request.method == "POST" and 'submit' in request.POST or 'draft' in request.POST:
        packsize = request.POST["packsize"]
        netwt=request.POST["netwt"]
        avgwt=request.POST["avgwt"]
        grosswt=request.POST["grosswt"]
        plugwt=request.POST["plugwt"]
        stdwt=request.POST["stdwt"]
        minstdqtypercent=request.POST["minstdqtypercent"]
        minstdqty=request.POST["minstdqty"]
        maxstdqtypercent=request.POST["maxstdqtypercent"]
        maxstdqty=request.POST["maxstdqty"]
        remark=request.POST["remark"]
        instruction=request.POST["instruction"]

        #get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
        get_packagecard.Packsize = int(packsize)
        get_packagecard.MaterialNetWt = netwt
        get_packagecard.ContainerWt = avgwt
        get_packagecard.GrossWt = grosswt
        get_packagecard.CapAvgWt = plugwt
        get_packagecard.StdWt = stdwt
        get_packagecard.MinPercent = minstdqtypercent
        get_packagecard.MinStdWt = minstdqty
        get_packagecard.MacPercent = maxstdqtypercent
        get_packagecard.MaxStdWt = maxstdqty
        get_packagecard.Remark =remark
        get_packagecard.Instructions =instruction

        get_packagecard.save()
        return redirect(packaging)

    if "Discard" in request.POST:
        print("In the discardd")
        status = request.POST["Discard"]
        get_packagecard.PackageCardApproval = status
        return redirect(packaging)


    if "Approve" in request.POST:
        print("In the Approveeeee")
        status = request.POST["Approve"]
        get_packagecard.PackageCardApproval = status
        ebc_list = ["create", get_packagecard.Created_By, "Package Card Approved", get_packagecard.PackageCardNo,
                    "viewpackaging"]
        notifications = notification("packaging_operator", ebc_list)


        BatchCardNumber = get_packagecard.BatchCardNo
        #get_batchcard = Batch_Card.objects.get(BatchCardNo=BatchCardNumber)
        ProductName = get_packagecard.Chemical_name
        PackageCardNumber = get_packagecard.PackageCardNo
        CreatedBy = get_packagecard.Created_By
        PackSize = get_packagecard.Packsize
        ProductionCount = get_packagecard.ProductionCount
        ShiftName = get_packagecard.ShiftName
        LineNo = get_packagecard.LineName
        Units_Box = get_packagecard.Units_Box
        bpm = get_packagecard.bpm
        shift_details = Shift.objects.get(shift = ShiftName)
        shift_starttime = shift_details.starttime
        shift_endtime = shift_details.endtime
        mssql(ProductName, BatchCardNumber, PackageCardNumber, CreatedBy, PackSize, ProductionCount, ShiftName, shift_starttime, shift_endtime, LineNo, Units_Box, bpm)

        get_packagecard.save()
        noti=notifications_db.objects.get(id=1).packaging_shiftincharge
        # ['packaging_shiftincharge']
        # print('noti',noti)
        noti=ast.literal_eval(noti)
        pno=PackageCardNumber
        url='editpackaging'
        new={}
        for d in noti:
            if d['view'] == pno and d['url'] == url:
                new = d
        delete_notification(request,str(new))

        return redirect(packaging)
    return render(request, 'editpackaging.html',{"get_packagecard":get_packagecard,"user_permissions":user_permissions,"notifications":notifications})



@login_required(login_url='login')
def viewpackaging(request, packagecardno):
    get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
    return render(request, 'viewpackaging.html',{"get_packagecard":get_packagecard})



@login_required(login_url='login')
def newproductionplanning(request):
    return render(request, 'newproductionplanning.html')


@login_required(login_url='login')
def productionplanning(request):
    return render(request, 'productionplanning.html')


@login_required(login_url='login')
def newproduction(request, packagecardno):
    get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
    get_batchcard = Batch_Card.objects.get(BatchCardNo=get_packagecard.BatchCardNo)
    add_pack = ast.literal_eval(get_packagecard.add_package)

    if request.method=="POST" and "complete" in request.POST:
        status = request.POST["complete"]
        get_packagecard.PackageCardApproval = status
        get_packagecard.save()
        return redirect(packaging)


    if request.method=="POST":
        plugging = request.POST["plugging"]
        induction_sealing=request.POST["induction_sealing"]
        leakage_testing=request.POST["leakage_testing"]
        bottle_testing = request.POST["bottle_testing"]
        sleeve_packing=request.POST["sleeve_packing"]
        remark = request.POST["remark"]

        #add_pack = ast.literal_eval(get_packagecard.add_package)
        add_pack.append({
            "plugging":plugging,
            "induction_sealing":induction_sealing,
            "leakage_testing":leakage_testing,
            "bottle_testing":bottle_testing,
            "sleeve_packing":sleeve_packing,
            "remark":remark,
            "timestamp":datetime.datetime.now().isoformat()
        })
        get_packagecard.add_package = add_pack
        get_packagecard.plugging+=int(plugging)
        get_packagecard.induction_sealing+=int(induction_sealing)
        get_packagecard.leakage_testing+=int(leakage_testing)
        get_packagecard.bottle_testing+=int(bottle_testing)
        get_packagecard.sleeve_packing+=int(sleeve_packing)
        get_packagecard.save()

    return render(request, 'newproduction.html',{"get_packagecard":get_packagecard,"get_batchcard":get_batchcard,"add_pack":add_pack})


@login_required(login_url='login')
def completepackagecard(request, packagecardno):

    user_permissions = role_checker(request, "packagecard_status")[0]

    get_packagecard = PackageCard.objects.get(PackageCardNo=packagecardno)
    get_packagecard.PackageCardApproval = "Completed"
    get_packagecard.save()
    return redirect(packaging)

def productionreport(request):
    return render(request, 'productionreport.html')

def printbatchcard(request):
    return render(request, 'printbatchcard.html')

def linenumber(request):
    return render(request, "linenumber.json")