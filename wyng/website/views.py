from django.shortcuts import render
from tablib import Dataset
from .resources import whsStgResource,whsMstResource ,whsInventoryResource ,stgMstResource ,stgInventoryResource ,prodMstResource,replenishment,required_qty
from .models import whs_mst,whs_stg,stg_inventory,whs_inventory,stg_mst,prod_mst
from django.http import HttpRequest,HttpResponse
import io, json
import csv

def index(request):
    return render(request, "import.html")


def product_mst_upload(request):
    if request.method == 'POST':
        prodmst_resource = prodMstResource()
        dataset = Dataset()
        uploaded_file = request.FILES['myfile']
        decoded_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(decoded_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = prod_mst.objects.create(
                Product_Code = column[0]
            )
    return render(request, 'core/simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        uploaded_file = request.FILES['myfile']
        decoded_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(decoded_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = prod_mst.objects.create(
                Product_Code=column[0]
            )

    return render(request, 'core/simple_upload.html')
# Create your views here.



def whs_stg_upload(request):
    if request.method == 'POST':
        whsStg_resource = whsStgResource()
        dataset = Dataset()
        uploaded_file = request.FILES['myfile']
        decoded_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(decoded_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = whs_stg.objects.create(
                WH = column[0],
                Store_Code = column[1]
            )

    return render(request, 'core/simple_upload.html')

def whs_mst_upload(request):
    if request.method == 'POST':
        whsStg_resource = whsMstResource()
        dataset = Dataset()
        uploaded_file = request.FILES['myfile']
        decoded_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(decoded_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = whs_mst.objects.create(
                WH=column[0],
            )

    return render(request, 'core/simple_upload.html')

def whs_inventory_upload(request):
    if request.method == 'POST':
        whsStg_resource = whsInventoryResource()
        dataset = Dataset()
        uploaded_file = request.FILES['myfile']
        decoded_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(decoded_data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = whs_inventory.objects.create(
                Product_Code=column[0],
                Store_Code = column[1],
                Date = column[2]
            )

    return render(request, 'core/simple_upload.html')

def storage_mst_upload(request):
    if request.method == 'POST':
        whsStg_resource = stgMstResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        new_persons2 = new_persons.read().decode('UTF-8')
        io_string = io.StringIO(new_persons2)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = stg_mst.objects.create(
                Store_Code=column[0]
            )
        # imported_data = dataset.load(new_persons2)
        # result = whsStg_resource.import_data(dataset, dry_run=True)  # Test the data import
        # if not result.has_errors():
        #     whsStg_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def stg_inventory_upload(request):
    if request.method == 'POST':
        whsStg_resource = stgInventoryResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        new_persons2 = new_persons.read().decode('UTF-8')
        io_string = io.StringIO(new_persons2)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created = stg_inventory.objects.create(
                Store_Code=column[0],
                Product_Code = column[1],
                Closing_Inventory = column[2],
                Date = column[3]
            )


    return render(request, 'core/simple_upload.html')



def exportrepl(request):
    person_resource = replenishmentResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

def exportreqd(request):
    person_resource = required_qtyResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response