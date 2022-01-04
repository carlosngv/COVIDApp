from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

from .models import (
    CSV,
    Report
    )

from .forms import (
    PredictionSelectionForm,
    Case1ParametersForm,
    Case4ParametersForm,
    Case5ParametersForm,
    Case6ParametersForm,
    Case7ParametersForm,
    Case8ParametersForm,
    Case9ParametersForm,
    Case10ParametersForm,
    Case25ParametersForm,
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
    global problem_solved

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

                if problem == '#1' or problem == '#2':
                    print("Generating problem 1 form...")
                    countries = df['Pais'].unique()
                    case1_form = Case1ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case1_form'] = case1_form
                elif problem == '#4':
                    print("Generating problem 4 form...")
                    countries = df['Pais'].unique()
                    case4_form = Case4ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case4_form'] = case4_form
                elif problem == '#5':
                    print("Generating problem 5 form...")
                    countries = df['Pais'].unique()
                    case5_form = Case5ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case5_form'] = case5_form
                elif problem == '#6':
                    print("Generating problem 6 form...")
                    countries = df['Pais'].unique()
                    date_choices = df['Dia'].unique()
                    case6_form = Case6ParametersForm(df_columns, countries, date_choices, request.POST or None, use_required_attribute=False)
                    context['case6_form'] = case6_form
                elif problem == '#7':
                    print("Generating problem 7 form...")
                    countries = df['Pais'].unique()
                    case7_form = Case7ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case7_form'] = case7_form
                elif problem == '#8':
                    print("Generating problem 8 form...")
                    countries = df['Pais'].unique()
                    case8_form = Case8ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case8_form'] = case8_form
                elif problem == '#9':
                    print("Generating problem 8 form...")
                    countries = df['Pais'].unique()
                    case9_form = Case9ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case9_form'] = case9_form
                elif problem == '#10':
                    print("Generating problem 10 form...")
                    countries = df['Pais'].unique()
                    case10_form = Case10ParametersForm(df_columns, countries, request.POST or None, use_required_attribute=False)
                    context['case10_form'] = case10_form
                elif problem == '#25':
                    print("Generating problem 25 form...")
                    case25_form = Case25ParametersForm(df_columns, request.POST or None, use_required_attribute=False)
                    context['case25_form'] = case25_form
                problem_solved = False


        elif 'predictBtn' in request.POST:
            if problem == '#1' or problem == '#2' :
                print('case 1')
                infected = request.POST.get('infected')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                days_to_predict = request.POST.get('days_to_predict')
                degree_number = request.POST.get('degree_number')
                variables = (infected, dates, country, days_to_predict, degree_number)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#4':
                print('case 4')
                deaths = request.POST.get('deaths')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                department = request.POST.get('department')
                days_to_predict = request.POST.get('days_to_predict')
                degree_number = request.POST.get('degree_number')
                variables = (deaths, dates, country, department, days_to_predict, degree_number)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#5':
                print('case 5')
                deaths = request.POST.get('deaths')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                days_to_predict = request.POST.get('days_to_predict')
                degree_number = request.POST.get('degree_number')
                variables = (deaths, dates, country, days_to_predict, degree_number)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#6':
                print('case 6')
                deaths = request.POST.get('deaths')
                dates = request.POST.get('date')
                country = request.POST.get('country')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')
                country_param = request.POST.get('country_param')
                variables = (deaths, dates, country, start_date, end_date, country_param)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#7':
                print('case 7')
                infected = request.POST.get('infected')
                dates = request.POST.get('date')
                country_param = request.POST.get('country_param')
                country = request.POST.get('country')
                variables = (infected, dates, country, country_param)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#8':
                print('case 8')
                infected = request.POST.get('infected')
                dates = request.POST.get('date')
                country_param = request.POST.get('country_param')
                country = request.POST.get('country')
                degree_number = request.POST.get('degree_number')
                variables = (infected, dates, country, country_param, degree_number)
                #print('DF: {}'.format(df))
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#9':
                print('case 9')
                vaccinated = request.POST.get('vaccinated')
                country_param = request.POST.get('country_param')
                country = request.POST.get('country')
                days_to_predict = request.POST.get('days_to_predict')
                degree_number = request.POST.get('degree_number')
                variables = (vaccinated, country, country_param, days_to_predict, degree_number)
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#10':
                print('case 10')
                vaccinated = request.POST.get('vaccinated')
                country_param = request.POST.get('country_param')
                country1 = request.POST.get('country1')
                country2 = request.POST.get('country2')
                days_to_predict = request.POST.get('days_to_predict')
                degree_number = request.POST.get('degree_number')
                variables = (vaccinated, country1, country2, country_param, days_to_predict, degree_number)
                resolve_problem(problem, df, variables)
                problem_solved = True
            elif problem == '#25':
                print('case 25')
                cases = request.POST.get('cases')
                date = request.POST.get('date')
                variables = (cases, date)
                resolve_problem(problem, df, variables)
                problem_solved = True

    context['problem_solved'] = problem_solved
    print('Problem selected: ', problem)
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
