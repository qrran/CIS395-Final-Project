from django.shortcuts import render, redirect

from .form import CreateRecordForm, UpdateRecordForm, CreateCommunityEngagementForm, UpdateCommunityEngagementForm

from .models import Record, CommunityEngagement



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

    return redirect("")


def ceTable(request):

    community_engagements = CommunityEngagement.objects.all()
    return render(request, 'webapp/ceTable.html', {'community_engagements': community_engagements})



# - CommunityEngagement Create
def createCERecord(request):
    if request.method == "POST":
        form2 = CreateCommunityEngagementForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("")
    else:
        form2 = CreateCommunityEngagementForm()
    
    context = {'form2': form2}
    return render(request, 'webapp/createCE.html', context=context)

# - Update a record 
def updateCERecord(request, pk):
    record2 = CommunityEngagement.objects.get(pk)

    if request.method == 'POST':
        form2 = UpdateCommunityEngagementForm(request.POST, instance=record2)
        if form2.is_valid():
            form2.save()
            return redirect("")
    else:
        form2 = UpdateCommunityEngagementForm(instance=record2)

    context = {'form2': form2}
    return render(request, 'webapp/updateCE.html', context=context)

def viewCE(request, pk):
    record2 = CommunityEngagement.objects.get(id2=pk)
    context = {'record2': record2}
    return render(request, 'webapp/viewCE.html', context=context)

# - Delete a record
def deleteCERecord(request, pk):
    record2 = CommunityEngagement.objects.get(pk)
    record2.delete()
    return redirect("")

def viewdetail(request):

    return render(request, 'webapp/viewdetail.html')