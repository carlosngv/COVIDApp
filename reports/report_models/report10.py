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

# 10
def vaccinated_comparison_country(df, variables, problem):
    plt.switch_backend('AGG')
    global actual_problem
    actual_problem = problem

    days_count=[]
    days_count2=[]
    target = variables[0] # Vaccinated
    country1 = variables[1]
    country2 = variables[2]
    country_param = variables[3]
    days_to_predict = int(variables[4])
    degree_number = int(variables[5])
    # Fitlering by country
    country1_selected_df = df.loc[df[country_param] == country1]
    vaccinated1_df = len(country1_selected_df[target])

    # Fitlering by country2
    country2_selected_df = df.loc[df[country_param] == country2]
    vaccinated2_df = len(country2_selected_df[target])


    # Storing days count
    for i in range (0, vaccinated1_df):
        days_count.append(i)

    for i in range (0, vaccinated2_df):
        days_count2.append(i)

    X = np.asarray(days_count)[0:days_to_predict + 1]
    Y = country1_selected_df[target][0:days_to_predict + 1]
    X2 = np.asarray(days_count2)[0:days_to_predict + 1]
    Y2 = country2_selected_df[target][0:days_to_predict + 1]
    plt.scatter(X, Y)
    plt.scatter(X2, Y2, c='coral')

    X = X[:, np.newaxis]
    Y = Y[:, np.newaxis]
    X2 = X2[:, np.newaxis]
    Y2 = Y2[:, np.newaxis]

    # Setting polynomial degree
    nb_degree=int(degree_number)
    polynomial_features=PolynomialFeatures(degree=nb_degree)
    polynomial_features2=PolynomialFeatures(degree=nb_degree)
    X_TRANSF=polynomial_features.fit_transform(X)
    X_TRANSF2=polynomial_features2.fit_transform(X2)

    model= LinearRegression()
    model2= LinearRegression()
    model.fit(X_TRANSF,Y)

    Y_NEW = model.predict(X_TRANSF)
    rmse=np.sqrt(metrics.mean_squared_error(Y,Y_NEW))

    r2=metrics.r2_score(Y,Y_NEW)
    x_new_main=0.0
    x__new_max=float(days_to_predict)


    X_NEW=np.linspace(x_new_main,x__new_max,50)

    X_NEW=X_NEW[:,np.newaxis]
    X_NEW_TRANSF =polynomial_features.fit_transform(X_NEW)
    Y_NEW=model.predict(X_NEW_TRANSF)
    prediction_value = Y_NEW[int(Y_NEW.size - 1)][0]

    # ==========================
    # Country 2 calculations
    model2.fit(X_TRANSF2,Y2)

    Y_NEW2 = model2.predict(X_TRANSF2)
    rmse=np.sqrt(metrics.mean_squared_error(Y2,Y_NEW2))

    r2=metrics.r2_score(Y2,Y_NEW2)
    x_new_main=0.0
    x__new_max=float(days_to_predict)

    X_NEW2=np.linspace(x_new_main,x__new_max,50)
    X_NEW2=X_NEW2[:,np.newaxis]
    X_NEW_TRANSF2 =polynomial_features2.fit_transform(X_NEW2)
    Y_NEW2=model2.predict(X_NEW_TRANSF2)
    prediction_value2 = Y_NEW2[int(Y_NEW2.size - 1)][0]

    # ==================================

    plt.plot(X_NEW2,Y_NEW2,color='red',label=country2)
    plt.plot(X_NEW,Y_NEW,color='black',label=country1)
    plt.grid()
    title='Grado={}; RMSE ={}; R2 ={}'.format(degree_number,round(rmse,2),round(r2,2))
    plt.title('Comparación tendencia en vacunación: ' + country1.upper() + ' Y ' + country2.upper() + '\n' + title)
    plt.xlabel('Días')
    plt.ylabel('Vacunados')
    plt.legend((country1, country2), loc='upper right')
    if prediction_value > prediction_value2:
        description = ''' \n
        La tendencia de personas vacunadas en el paìs de {} para los siguientes {} días indica que el numero de
        vacunados tiende a decrecer conforme pasan los días en comparación del país {} cuya relación días/vacunados tiende a crecer más lento.
        '''.format(country1, days_to_predict, country2)
    else:
        description = ''' \n
        La tendencia de personas vacunadas en el paìs de {} para los siguientes {} días indica que el numero de
        vacunados tiende a decrecer conforme pasan los días en comparación del país {} cuya relación días/vacunados tiende a crecer más lento.
        '''.format(country2, days_to_predict, country1)
    save_report(description)
