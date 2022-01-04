from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

import base64
import pandas as pd
import numpy as np
from io import BytesIO

from ..models import Report
from ..shared import PREDICTION_CHOICES

actual_problem = ''

def get_report_name(prediction_selected):
    for prediction in PREDICTION_CHOICES:
        if prediction[0] == prediction_selected:
            return prediction[1]
    return ''

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def save_report(description):
    report_name = get_report_name(actual_problem)

    chart = get_graph()

    if Report.objects.filter(name=actual_problem).exists():
        report = Report.objects.get(name=actual_problem)
        report.description = description
        report.image_str = chart
        report.title=report_name
        report.save()
        print('MODIFIED report: {}'.format(report))
    else:
        new_report = Report(name=actual_problem, title=report_name, image_str=chart, description=description)
        new_report.save()
        print('NEW report: {}'.format(new_report))
    return chart

# 15
def activecases_trend_department(df, variables, problem):
    plt.switch_backend('AGG')
    global actual_problem
    actual_problem = problem

    days_count=[]
    target = variables[0] # infected
    country_param = variables[1]
    country = variables[2]
    department_param = variables[3]
    department = variables[4]
    days_to_predict = int(variables[5])
    degree_number = int(variables[6])

    # Fitlering by department
    df = df.loc[df[country_param] == country]
    department_selected_df = df.loc[df[department_param] == department]
    cases_df = len(department_selected_df[target])
    #print('countries:',department_selected_df)

    # Storing days count
    for i in range (0, cases_df):
        days_count.append(i)

    X = np.asarray(days_count)[0:days_to_predict + 1]
    Y = department_selected_df[target][0:days_to_predict + 1]
    X_scatter = X
    Y_scatter = Y

    X = X[:, np.newaxis]
    Y = Y[:, np.newaxis]

    # Setting polynomial degree

    polynomial_features=PolynomialFeatures(degree=degree_number)
    X_TRANSF=polynomial_features.fit_transform(X)

    reg= LinearRegression()
    reg.fit(X_TRANSF,Y)

    Y_NEW = reg.predict(X_TRANSF)
    rmse=np.sqrt(metrics.mean_squared_error(Y,Y_NEW))

    r2=metrics.r2_score(Y,Y_NEW)
    x_new_main=0.0
    x__new_max=float(days_to_predict)


    X_NEW=np.linspace(x_new_main,x__new_max,50)

    X_NEW=X_NEW[:,np.newaxis]
    X_NEW_TRANSF =polynomial_features.fit_transform(X_NEW)

    Y_NEW=reg.predict(X_NEW_TRANSF)
    initial_prediction_value = Y_NEW[0][0]
    prediction_value = Y_NEW[int(Y_NEW.size - 1)][0]

    plt.plot(X_NEW,Y_NEW,color='black',linewidth=2)
    plt.scatter(X_scatter, Y_scatter)

    intercept = reg.intercept_[0] # X
    coef = reg.coef_[0][0] # Y


    title='Grado={}; RMSE ={}; R2 ={}'.format(degree_number,round(rmse,2),round(r2,2))
    plt.title(country.upper() + ', ' + department.upper() + '\n' + title)
    plt.xlabel('Días')
    plt.ylabel('Casos confirmados')
    plt.legend(('Data','Polynomial Regression'), loc='upper right')
    if initial_prediction_value > prediction_value:
        description = ''' \n
        La tendencia de casos confirmados en el departamento de {} en el país de {} para los siguientes {} días es de {} e indica que el numero de
        muertes decrece conforme pasan los días.
        '''.format(department, country, days_to_predict, prediction_value)
    else:
        description = ''' \n
        La tendencia de casos confirmados en el departamento de {} en el país de {} para los siguientes {} días es de {} e indica que el numero de
        muertes crece conforme pasan los días.
        '''.format(department, country, days_to_predict, prediction_value)
    save_report(description)
