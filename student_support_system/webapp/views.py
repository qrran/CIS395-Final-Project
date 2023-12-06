from django.shortcuts import render, redirect

from .form import CreateRecordForm, UpdateRecordForm

from .models import Record



def home(request):

    # return HttpResponse('new page') homePage

    return render(request, 'webapp/index.html')

# - Dashboard

def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


# - Create a record 

def createRecord(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")

    context = {'form': form}
    # context ={'key'(same on in createRecord.html : form}

    return render(request, 'webapp/createRecord.html', context=context)
    # has to be the same html name as the html file

# - Update a record 

def updateRecord(request, pk):

    pass

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'webapp/updateRecord.html', context=context)


# - Read / View a singular record

def viewRecord(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/viewRecord.html', context=context)


# - Delete a record

def deleteRecord(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")
