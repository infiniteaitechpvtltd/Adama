from django.db import models


class User_Data(models.Model):
    objects = models.Manager()
    Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    User_Role = models.CharField(max_length=30)
    Shift = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    plant_name = models.CharField(max_length=30)
    line_name = models.CharField(max_length=30)
    process = models.CharField(max_length=30, default="Formulation")

    def __str__(self):
        return self.Username


class Shift(models.Model):
    objects = models.Manager()
    shift = models.CharField(max_length=30)
    starttime = models.CharField(max_length=50, default="")
    endtime = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.shift

class Sample(models.Model):
    objects = models.Manager()
    sample_types = models.CharField(max_length=30)

    def __str__(self):
        return self.sample_types


class Tank(models.Model):
    objects = models.Manager()
    tank = models.CharField(max_length=30)

    def __str__(self):
        return self.tank


class Chemical(models.Model):
    objects = models.Manager()
    Brand_Name = models.CharField(max_length=30)
    Brand_No = models.CharField(max_length=30)
    SAP_Code = models.CharField(max_length=30)
    SPGR = models.FloatField(default=0)
    Chemical_name = models.CharField(max_length=100)
    Base_Calc = models.CharField(max_length=30,default="Batch_Size")
    Raw_Materials = models.TextField(max_length=5000)
    Technicals = models.TextField(max_length=500)
    product_category = models.CharField(max_length=30)
    expiry = models.IntegerField()
    Type = models.CharField(max_length=30,default="Liquid")


    def __str__(self):
        return self.Brand_Name


class Batch_Card(models.Model):
    objects = models.Manager()
    ShiftName = models.CharField(max_length=20)
    Created_Date = models.CharField(max_length=30)
    Product_Category = models.CharField(max_length=30)
    BatchCardNo = models.CharField(max_length=30)
    Brand_Name = models.CharField(max_length=30)
    Brand_No = models.CharField(max_length=30)
    Batch_Size = models.IntegerField()
    Tank_Num = models.CharField(max_length=30)
    Plant_Name = models.CharField(max_length=30, default="")
    THBatch_Size = models.IntegerField()
    SAP_Code = models.CharField(max_length=30)
    SPGR = models.FloatField()
    Chemical_name = models.CharField(max_length=100,default="")
    Base_Calc = models.CharField(max_length=30, default="Batch_Size")
    Technicals = models.TextField(max_length=500,default="[]")
    Raw_Materials = models.TextField(max_length=5000,default="[]")
    Created_By=models.CharField(max_length=30,default="")
    MFG_Date = models.CharField(max_length=30,default="")
    Expiry = models.IntegerField(default=0)
    Expiry_Date = models.CharField(max_length=30,default="")
    Remark = models.CharField(max_length=100,default="")
    BatchCard_Approval = models.CharField(max_length=30, default="Pending")
    Approved_By=models.CharField(max_length=30,default="")
    Approved_Date=models.CharField(max_length=50,default="")
    BatchCard_Status = models.CharField(max_length=30, default="Pending")
    Add_Chemical = models.TextField(max_length=10000,default="[]")
    Add_Sample=models.TextField(max_length=1000,default="[]")

    def __str__(self):
        return self.BatchCardNo


class PackageCard(models.Model):
    objects = models.Manager()
    BatchCardNo = models.CharField(max_length=30)
    PackageCardNo = models.CharField(max_length=30)
    ShiftName = models.CharField(max_length=20)
    LineName = models.CharField(max_length=30)
    Created_Date = models.CharField(max_length=30)
    Chemical_name = models.CharField(max_length=100)
    Plant_Name = models.CharField(max_length=30, default="Herbicide")
    SPGR = models.FloatField(default=0.0)
    Packsize = models.IntegerField(default=0)
    MaterialNetWt = models.FloatField(default=0.0)
    BoxType = models.CharField(max_length=30,default=0)
    Units_Box = models.IntegerField(default=0)
    ProductionCount = models.IntegerField(default=0)
    ContainerWt = models.FloatField(default=0.0)
    GrossWt = models.FloatField(default=0.0)
    CapAvgWt = models.FloatField(default=0.0)
    StdWt = models.FloatField(default=0.0)
    MinPercent = models.FloatField(default=0.0)
    MinStdWt = models.FloatField(default=0.0)
    MacPercent = models.FloatField(default=0.0)
    MaxStdWt = models.FloatField(default=0.0)
    Remark = models.CharField(max_length=200)
    Instructions = models.CharField(max_length=200)
    Created_By = models.CharField(max_length=30)
    machine_speed = models.CharField(max_length=30)
    bpm=models.CharField(max_length=30)
    nozzle_two = models.CharField(max_length=30)
    nozzle_three = models.CharField(max_length=30)
    nozzle_four = models.CharField(max_length=30)
    nozzle_five = models.CharField(max_length=30)
    nozzle_six = models.CharField(max_length=30)
    plugging = models.IntegerField(default=0)
    induction_sealing =models.IntegerField(default=0)
    leakage_testing=models.IntegerField(default=0)
    bottle_testing=models.IntegerField(default=0)
    sleeve_packing=models.IntegerField(default=0)
    add_package = models.TextField(max_length=1000,default=[])
    PackageCardApproval = models.CharField(max_length=30,default="Pending")
    Approved_By = models.CharField(max_length=30,default="")
    Approved_Date = models.CharField(max_length=30,default="")
    PackageCardStatus = models.CharField(max_length=30,default="Pending")


    def __str__(self):
        return '%s %s %s' %(self.PackageCardNo,self.Created_Date,self.PackageCardApproval)


class Operator_Role(models.Model):
    objects = models.Manager()
    batch_cards_one = models.BooleanField()
    batch_cards_two = models.BooleanField()
    tasks_one = models.BooleanField()
    tasks_two = models.BooleanField()
    maintenance_one = models.BooleanField()
    maintenance_two = models.BooleanField()
    sops_one = models.BooleanField()
    sops_two = models.BooleanField()
    alarms_one = models.BooleanField()
    alarms_two = models.BooleanField()
    profiles_one = models.BooleanField()
    profiles_two = models.BooleanField()
    mp_plan_one = models.BooleanField()
    mp_plan_two = models.BooleanField()
    prod_plan_one = models.BooleanField()
    prod_paln_two = models.BooleanField()


class Shift_Incharge_Role(models.Model):
    objects = models.Manager()
    batch_cards_one = models.BooleanField()
    batch_cards_two = models.BooleanField()
    tasks_one = models.BooleanField()
    tasks_two = models.BooleanField()
    maintenance_one = models.BooleanField()
    maintenance_two = models.BooleanField()
    sops_one = models.BooleanField()
    sops_two = models.BooleanField()
    alarms_one = models.BooleanField()
    alarms_two = models.BooleanField()
    profiles_one = models.BooleanField()
    profiles_two = models.BooleanField()
    mp_plan_one = models.BooleanField()
    mp_plan_two = models.BooleanField()
    prod_plan_one = models.BooleanField()
    prod_paln_two = models.BooleanField()


class Line_Incharge_Role(models.Model):
    objects = models.Manager()
    batch_cards_one = models.BooleanField()
    batch_cards_two = models.BooleanField()
    tasks_one = models.BooleanField()
    tasks_two = models.BooleanField()
    maintenance_one = models.BooleanField()
    maintenance_two = models.BooleanField()
    sops_one = models.BooleanField()
    sops_two = models.BooleanField()
    alarms_one = models.BooleanField()
    alarms_two = models.BooleanField()
    profiles_one = models.BooleanField()
    profiles_two = models.BooleanField()
    mp_plan_one = models.BooleanField()
    mp_plan_two = models.BooleanField()
    prod_plan_one = models.BooleanField()
    prod_plan_two = models.BooleanField()

class SOP(models.Model):
    objects = models.Manager()
    created_date = models.CharField(max_length=30)
    sop_name = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    sop_category = models.CharField(max_length=50)
    file = models.FileField()
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.sop_name


class CreateTask(models.Model):
    objects = models.Manager()
    shift = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    assigned = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default="InProgress")
    comment = models.CharField(max_length=500)
    created_date = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    completed_date = models.CharField(max_length=30)

    def __str__(self):
        return self.task

class Tasks_list(models.Model):
    objects = models.Manager()
    Tasks = models.CharField(max_length=50)

    def __str__(self):
        return self.Tasks


class Plant_Detail(models.Model):
    objects = models.Manager()
    PlantName = models.CharField(max_length=100)
    ContractorDetails = models.TextField()
    AllotmentDetails = models.CharField(max_length=100)
    LineDetails = models.CharField(max_length=100)
    MachineDetails = models.CharField(max_length=100)

    def __str__(self):
        return self.ContractorDetails


class Plant_List(models.Model):
    objects = models.Manager()
    PlantName = models.CharField(max_length=100)
    LineDetails = models.TextField()

    def __str__(self):
        return self.PlantName

class ManPower_Detail(models.Model):
    objects = models.Manager()
    CreatedDate = models.CharField(max_length=30)
    AllottedDate = models.CharField(max_length=30)
    shift = models.CharField(max_length=30)
    contractor = models.CharField(max_length=30)
    allotment = models.CharField(max_length=30)
    noofalotment = models.CharField(max_length=30)
    plant = models.CharField(max_length=30)

    def __str__(self):
        return self.contractor


class Maintenance_Detail(models.Model):
    objects = models.Manager()
    startdatetime = models.CharField(max_length=30)
    maintenancetype = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    plant = models.CharField(max_length=30)
    line = models.CharField(max_length=30)
    machine = models.CharField(max_length=30)
    equipment = models.CharField(max_length=30)
    part = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    enddatetime = models.CharField(max_length=30)
    reason = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)

    def __str__(self):
        return self.equipment

class notifications_db(models.Model):
    objects = models.Manager()
    formulation_operator = models.TextField(default=[])
    packaging_operator = models.TextField(default=[])
    formulation_shiftincharge = models.TextField(default=[])
    packaging_shiftincharge = models.TextField(default=[])
    formulation_lineincharge = models.TextField(default=[])
    packaging_lineincharge = models.TextField(default=[])
    admin = models.TextField(default=[])

