from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from matplotlib.pyplot import clf

from .models import (
    CSV,
    Report
    )

from .forms import (
    PredictionSelectionForm,
    Case5ParametersForm
    )

from .utils import (
    resolve_problem
)


import pandas as pd
import csv
import io

actual_csv = ''
file_content = ''
prediction = ''
df = None

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'

def csv_upload_view(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        global file_content
        file_content = request.FILES.get('file').read()
        file_content = file_content.decode('utf-8')


        obj = CSV.objects.create(file_name=csv_file)
        global actual_csv
        actual_csv = obj.file_name.path
        #actual_csv = csv_file

        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            reader.__next__() # Skips the first row (without columns)
            for row in reader:
                pass
                #print(row)

    return HttpResponse()

def home_view(request):
    df_html = None
    df_columns = None
    global df
    global prediction
    print("prediction: {}".format(prediction))

    form = PredictionSelectionForm(request.POST or None)

    context = {
        'df': df_html,
        'form': form,
        'file_content': file_content,
        'prediction': prediction,
        'chart': ''
    }

    if request.method == 'POST':

        if 'selectBtn' in request.POST:
            print('case 0')
            prediction = request.POST.get('prediction')
            context['prediction'] = prediction

            if file_content != '':
                df = pd.read_csv(io.StringIO(file_content), sep=",")
                df_columns = df.columns.tolist()
                context['columns'] = df_columns
                df_html = df.to_html(classes=['table', 'table-primary'])
                context['df'] = df_html

                if prediction == '#5':
                    #countries = df.drop_duplicates(subset=['country'])
                    countries = df['country'].unique()
                    print(countries)
                    case5_form = Case5ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case5_form'] = case5_form

        elif 'predictBtn' in request.POST:
            if prediction == '#5':
                print('case 5')
                deaths = request.POST.get('deaths')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                variables = (deaths, dates, country)
                print('DF: {}'.format(df))
                chart = resolve_problem(prediction, df, variables)
                context['chart'] = chart
            elif prediction == '#1' :
                print('case 1')
                variables = ()
                resolve_problem(prediction, df, variables)
            elif prediction == '#2':
                print('case 2')
                variables = ()
                resolve_problem(prediction, df, variables)

    return render(request, 'reports/home.html', context)

def reports_view(request):
    msg = 'This is a message'
    return render(request, 'reports/reports.html', {'msg': msg})
