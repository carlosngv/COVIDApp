from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from .models import (
    CSV,
    Report
    )

from .forms import (
    PredictionSelectionForm,
    Case6ParametersForm
    )

from .utils import (
    resolve_problem
)


import pandas as pd
import io

actual_csv = ''
file_content = ''
problem = ''
df = None
problem_solved = False

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'

def csv_upload_view(request):
    if request.method == 'POST':
        #csv_file = request.FILES.get('file')
        global file_content
        file_content = request.FILES.get('file').read()
        file_content = file_content.decode('utf-8')


        # obj = CSV.objects.create(file_name=csv_file)
        # global actual_csv
        # actual_csv = obj.file_name.path
        # #actual_csv = csv_file

        # with open(obj.file_name.path, 'r') as f:
        #     reader = csv.reader(f)
        #     reader.__next__() # Skips the first row (without columns)
        #     for row in reader:
        #         pass
                #print(row)

    return HttpResponse()

def home_view(request):
    df_html = None
    df_columns = None
    global df
    global problem

    form = PredictionSelectionForm(request.POST or None)

    context = {
        'df': df_html,
        'form': form,
        'file_content': file_content,
        'problem': problem,
        'chart': ''
    }

    if request.method == 'POST':

        if 'selectBtn' in request.POST:
            print('case 0')
            problem = request.POST.get('problem')
            context['problem'] = problem

            if file_content != '':
                df = pd.read_csv(io.StringIO(file_content), sep=",")
                df_columns = df.columns.tolist()
                context['columns'] = df_columns
                df_html = df.to_html(classes=['table', 'table-primary'])
                context['df'] = df_html

                if problem == '#6':
                    print("Generating problem 6 form...")
                    countries = df['Pais'].unique()
                    date_choices = df['Dia'].unique()
                    case5_form = Case6ParametersForm(df_columns, countries, date_choices, request.POST or None, use_required_attribute=False)
                    context['case5_form'] = case5_form

        elif 'predictBtn' in request.POST:
            if problem == '#1' :
                print('case 1')
                variables = ()
                resolve_problem(problem, df, variables)
            elif problem == '#2':
                print('case 2')
                variables = ()
                resolve_problem(problem, df, variables)
            elif problem == '#6':
                print('case 6')
                deaths = request.POST.get('deaths')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')
                variables = (deaths, dates, country, start_date, end_date)
                #print('DF: {}'.format(df))
                chart = resolve_problem(problem, df, variables)
                context['chart'] = chart
    response = render(request, 'reports/home.html', context)
    response.set_cookie('problem', problem)
    return response

def reports_view(request):
    context = {}
    if 'problem' in request.COOKIES and request.COOKIES['problem'] != '':
        cookie_problem = request.COOKIES['problem']
        obj = Report.objects.filter(name=cookie_problem)[0]
        context['obj'] = obj
        context['problem'] = cookie_problem
    return render(request, 'reports/reports.html', context)
