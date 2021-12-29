from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from .models import CSV
from .forms import PredictionSelectionForm
from .utils import get_chart
import pandas as pd
import csv

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'

def csv_upload_view(request):
    print('File is being send')

    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        obj = CSV.objects.create(file_name=csv_file)
        print(obj)

        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            reader.__next__() # Skips the first row (without columns)
            for row in reader:
                print(row, type(row))

    return HttpResponse()

def home_view(request):
    df = None
    chart = None

    form = PredictionSelectionForm(request.POST or None)
    data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
    df = pd.DataFrame(data)

    df_html = df.to_html(classes=['table', 'table-dark'])

    context = {
        'df': df_html,
        'form': form,
    }




    if request.method == 'POST':
        prediction = request.POST.get('prediction')
        context['prediction'] = prediction
        chart = get_chart(prediction, df)
        context['chart'] = chart
        print(prediction)


    return render(request, 'reports/home.html', context)

def reports_view(request):
    msg = 'This is a message'
    return render(request, 'reports/reports.html', {'msg': msg})
