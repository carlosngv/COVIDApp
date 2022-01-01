import datetime
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile
from datetime import date
from sklearn.linear_model import LinearRegression
from io import BytesIO
from .models import Report


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

def save_report():
    report_name = get_report_name(actual_problem)
    description = 'Se ha concluido que el problema "{}" ha sido realizado exitosamente'.format(report_name)
    chart = get_graph()
    print('CHART = {}'.format(type(chart)))
    if Report.objects.filter(name=actual_problem).exists():
        report = Report.objects.get(name=actual_problem)
        report.description = description
        report.image_str = chart
        print('MODIFIED report: {}'.format(report))
    else:
        new_report = Report(name=actual_problem, image_str=chart, description=description)
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
def mortality_prediction_country(df, variables, problem):
    # local and global variables
    global actual_problem
    actual_problem = problem

    x = []
    dates = []
    new_labels = []
    target = variables[0] # Deaths
    date_features = variables[1] # Dates
    country = variables[2] # Country value

    # Preparing graph
    plt.switch_backend('AGG')
    _ = plt.figure(figsize=(7,2))

    # Formatting dates
    for csv_date in df[date_features]:
        dt = datetime.datetime.strptime(csv_date, "%d/%m/%Y").strftime("%m/%d/%Y")
        x.append(dt)

    x = pd.Series(x)

    df['date_ordinal'] = pd.to_datetime(x).apply(lambda date: date.toordinal())

    df2 = df.groupby(['date_ordinal', 'country'], as_index=False)[target].sum()
    df2 = df2.loc[df2['country'] == country]
    print(df2)

    X = np.asarray(df2['date_ordinal'])
    y = np.asarray(df2[target])

    reg = LinearRegression()

    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)


    reg.fit(X, y)
    prediction_space = np.linspace(min(X), max(X)).reshape(-1, 1)

    y_predict = reg.predict(prediction_space)
    #print('y_predict in linespace: {}'.format(y_predict))
    plt.scatter(X, y, color='black')
    plt.plot(prediction_space, reg.predict(prediction_space))
    plt.ylabel('Deaths')
    plt.xlabel('Days')



    for item in X:
        new_date = date.fromordinal(int(item))
        dates.append(new_date)

    for item in dates:
        new_labels.append(item.strftime("%d/%m/%Y"))

    new_labels = np.asarray(new_labels)
    plt.xticks(np.asarray(df2['date_ordinal']), labels=new_labels)
    return save_report()
# 6
def death_number_analysis():
    pass

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
