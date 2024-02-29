from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas


def home(request):
    myData = Datas.objects.all()
    return render(request, 'index.html')

def FetchData(request):
    if request.method == 'POST':
        userid = request.POST.get('userid') 
        file = request.POST.get('chosefile')

        try:
            # Attempt to get objects with the specified userId
            myData = Datas.objects.filter(userId=userid)

            mycoulmn = filedata.objects.filters(fileName=file)

            if myData.exists():
               
                return render(request, 'index.html', {'datas': myData})
            else:
                error_message = "No data found for the provided User ID."

        except Exception as e:
            #database error
            error_message = f"Error: {str(e)}"

    # If the request is not a POST request or an error occurs, render the form again
    return render(request, 'index.html', {'error_message': error_message})


 