from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .models import Report
import matplotlib.pyplot as plt
import datetime
import base64
import pandas as pd
import numpy as np
from datetime import date
from io import BytesIO


PREDICTION_CHOICES = (
    ('#1', 'Tendencia de la infección por Covid-19 en un País.'),
    ('#2', 'Predicción de Infertados en un País.'),
    ('#3', 'Indice de Progresión de la pandemia.'),
    ('#4', 'Predicción de mortalidad por COVID en un Departamento.'),
    ('#5', 'Predicción de mortalidad por COVID en un País.'),
    ('#6', 'Análisis del número de muertes por coronavirus en un País.'),
    ('#7', 'Tendencia del número de infectados por día de un País.'),
    ('#8', 'Predicción de casos de un país para un año.'),
    ('#9', 'Tendencia de la vacunación de en un País.'),
    ('#10', 'Ánalisis Comparativo de Vacunaciópn entre 2 paises.'),
    ('#11', 'Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo'),
    ('#12', 'Ánalisis Comparativo entres 2 o más paises o continentes.'),
    ('#13', 'Muertes promedio por casos confirmados y edad de covid 19 en un País.'),
    ('#14', 'Muertes según regiones de un país - Covid 19.'),
    ('#15', 'Tendencia de casos confirmados de Coronavirus en un departamento de un País.'),
    ('#16', 'Porcentaje de muertes frente al total de casos en un país, región o continente.'),
    ('#17', 'Tasa de comportamiento de casos activos en relación al número de muertes en un continente.'),
    ('#18', 'Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.'),
    ('#19', 'Predicción de muertes en el último día del primer año de infecciones en un país.'),
    ('#20', 'Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19'),
    ('#21', 'Predicciones de casos y muertes en todo el mundo - Neural Network MLPRegressor'),
    ('#22', 'Tasa de mortalidad por coronavirus (COVID-19) en un país.'),
    ('#23', 'Factores de muerte por COVID-19 en un país.'),
    ('#24', 'Comparación entre el número de casos detectados y el número de pruebas de un país.'),
    ('#25', 'Predicción de casos confirmados por día'),
)


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

# 1
def infection_trend_country():
    pass

# 2
def infection_prediction_country():
    pass

# 3
def epidemic_progression_progress():
    pass

# 4
def mortality_prediction_state():
    pass

# 5
def mortality_prediction_country():
    pass

# 6
def death_analysis_country(df, variables, problem):
    # local and global variables
    global actual_problem
    actual_problem = problem

    x = []
    dates = []
    new_labels = []
    target = variables[0] # Deaths
    date_features = variables[1] # Dates
    country = variables[2] # Country value
    start_date = variables[3]
    end_date = variables[4]

    # Preparing graph
    plt.switch_backend('AGG')
    _ = plt.figure(figsize=(7,2))

    # Formatting dates
    df[date_features] = pd.to_datetime(df[date_features], dayfirst=True, infer_datetime_format=True)

    # Processing date boundaries
    limit_dates = pd.to_datetime(np.asarray([start_date, end_date]), dayfirst=True, infer_datetime_format=True)
    ordinal_limit_dates = pd.to_datetime(limit_dates).to_series().apply(lambda date: date.toordinal())
    print('ordinal_limit_dates',ordinal_limit_dates)

    # Generating ordinal dates and filtering by country
    df['date_ordinal'] = pd.to_datetime(df[date_features]).apply(lambda date: date.toordinal())
    df = df.groupby(['date_ordinal', 'Pais'], as_index=False)['Muertes'].sum()
    df = df.loc[df['Pais'] == country]

    # Filtering dates
    df = df.loc[df['date_ordinal'] >= ordinal_limit_dates[0]]
    df = df.loc[df['date_ordinal'] <= ordinal_limit_dates[1]]


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
    plt.ylabel('Muertes')
    plt.xlabel('Días')


    intercept = reg.intercept_ # X
    coef = reg.coef_[0][0] # Y
    y_pred = reg.predict(X_test)
    print('y_pred', y_pred)

    mae = metrics.mean_absolute_error(y_test, y_pred)
    mse = metrics.mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

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

    title = 'Análisis en número de muertes en ' + country +'\n'+'Modelo entrenado: y = ' + str(coef) + 'X +' + str(intercept)
    plt.title("Regresión linear simple \n" + title, fontsize=10)
    plt.legend(('Linear Regression','Data'), loc='upper right')
    plt.locator_params(axis='x', nbins=5) # Reducing x axis bins
    if coef < 0:
        description = ''' \
        El coeficiente de regresión tiene un valor de: {}.  \

        El cuál indica que el numero de muertes ha disminuido conforme pasan los días en {}. \
        '''.format(coef, country)
    else:
        description = ''' \n
        El coeficiente de regresión tiene un valor de: {}. \n

        El cuál indica que el numero de muertes ha incrementado conforme pasan los días en {}.  \n
        '''.format(coef, country)
    return save_report(description)

# 7
def infection_trend_day_country():
    pass

# 8
def cases_prediction_year():
    # Predicción de casos para un año de un país
    pass

# 9
def mortality_country():
    pass
