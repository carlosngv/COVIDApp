from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

import base64
import pandas as pd
import numpy as np
from datetime import date
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


# 25
def confirmed_cases_prediction_byday(df, variables, problem):
    # local and global variables
    global actual_problem
    actual_problem = problem

    x = []
    dates = []
    new_labels = []
    target = variables[0] # Infected parameter name
    date_features = variables[1] # Dates parameter name
    # Preparing graph
    plt.switch_backend('AGG')
    _ = plt.figure(figsize=(7,2))

    # Formatting dates
    df[date_features] = pd.to_datetime(df[date_features], dayfirst=True, infer_datetime_format=True)


    # Generating ordinal dates and filtering by country
    df['date_ordinal'] = pd.to_datetime(df[date_features]).apply(lambda date: date.toordinal())
    df = df.groupby(['date_ordinal'], as_index=False)[target].sum()


    X = np.asarray(df['date_ordinal'])
    y = np.asarray(df[target])

    reg = LinearRegression()

    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    reg.fit(X_train, y_train)
    prediction_space = np.linspace(min(X_train), max(X_train)).reshape(-1, 1)
    y_predict = reg.predict(prediction_space)

    plt.scatter(X, y, color='black')
    plt.plot(prediction_space, y_predict)
    plt.ylabel('Casos confirmados')
    plt.xlabel('Días')


    intercept = reg.intercept_[0] # X
    coef = reg.coef_[0][0] # Y
    y_pred = reg.predict(X_test)
    print('y_pred', y_pred)

    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    r2 = reg.score(X_test, y_test)


    print('Mean Absolute Error:', mae)
    print('Mean Squared Error:', mse)
    print('Root Mean Squared Error:', rmse)

    for item in X:
        new_date = date.fromordinal(int(item))
        dates.append(new_date)

    for item in dates:
        new_labels.append(item.strftime("%d/%m/%Y"))

    new_labels = np.asarray(new_labels)
    plt.xticks(np.asarray(df['date_ordinal']), labels=new_labels)

    title = 'Casos confirmados por día' + '\n'+'Modelo entrenado: y = ' + str(coef) + 'X +' + '(' + str(intercept) + ')'
    plt.title("Regresión linear simple \n" + title, fontsize=6)
    plt.legend(('Data','Linear Regression'), loc='upper right')
    plt.locator_params(axis='x', nbins=5) # Reducing x axis bins
    if coef < 0:
        description = ''' \
        El coeficiente de regresión tiene un valor de: {}.  \

        El cuál indica que el numero de infectados ha disminuido conforme pasan los días. MSE = {}; RMSE = {}; R2 = {}
        '''.format(coef, round(mse,2),round(rmse,2),round(r2,2))
    else:
        description = ''' \n
        El coeficiente de regresión tiene un valor de: {}. \n

        El cuál indica que el numero de infectados ha incrementado conforme pasan los días.  MSE = {}; RMSE = {}; R2 = {}
        '''.format(coef, round(mse,2),round(rmse,2),round(r2,2))
    save_report(description)
