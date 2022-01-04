from django import forms
from .shared import PREDICTION_CHOICES

class PredictionSelectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PredictionSelectionForm, self).__init__(*args, **kwargs)
        self.fields['problem'].label = "Selecciona el problema a resolver"
    problem = forms.ChoiceField(choices=PREDICTION_CHOICES)

class Case1ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case1ParametersForm, self).__init__(*args, **kwargs)
        self.fields['infected'].required = False
        self.fields['infected'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['infected'].label = "Infectados"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a analizar"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"
    infected = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case4ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case4ParametersForm, self).__init__(*args, **kwargs)
        self.fields['deaths'].required = False
        self.fields['deaths'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['deaths'].label = "Muertes"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['department'].required = False
        self.fields['department'] = forms.CharField(max_length=120)
        self.fields['department'].label = "Departamento"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"
    deaths = forms.ChoiceField()
    country = forms.ChoiceField()
    department = forms.CharField()
    date = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case5ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case5ParametersForm, self).__init__(*args, **kwargs)
        self.fields['deaths'].required = False
        self.fields['deaths'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['deaths'].label = "Muertes"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"
    deaths = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()


class Case6ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries,date_choices, *args, **kwargs):
        super(Case6ParametersForm, self).__init__(*args, **kwargs)
        self.fields['deaths'].required = False
        self.fields['deaths'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['deaths'].label = "Muertes"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country_param'].label = "Parametro País"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['start_date'].required = False
        self.fields['start_date'] = forms.ChoiceField(choices=tuple([(param, param) for param in date_choices]))
        self.fields['start_date'].label = "Fecha inicio"
        self.fields['end_date'].required = False
        self.fields['end_date'] = forms.ChoiceField(choices=tuple([(param, param) for param in date_choices]))
        self.fields['end_date'].label = "Fecha fin"
    deaths = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()
    start_date = forms.ChoiceField()
    end_date = forms.ChoiceField()

class Case7ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case7ParametersForm, self).__init__(*args, **kwargs)
        self.fields['infected'].required = False
        self.fields['infected'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['infected'].label = "Infectados"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro País"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
    infected = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()

class Case8ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case8ParametersForm, self).__init__(*args, **kwargs)
        self.fields['infected'].required = False
        self.fields['infected'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['infected'].label = "Infectados"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"

    infected = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    date = forms.ChoiceField()
    degree_number = forms.ChoiceField()

class Case9ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case9ParametersForm, self).__init__(*args, **kwargs)
        self.fields['vaccinated'].required = False
        self.fields['vaccinated'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['vaccinated'].label = "Vacunados"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"

    vaccinated = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case10ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case10ParametersForm, self).__init__(*args, **kwargs)
        self.fields['vaccinated'].required = False
        self.fields['vaccinated'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['vaccinated'].label = "Vacunados"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country1'].required = False
        self.fields['country1'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country1'].label = "País 1"
        self.fields['country2'].required = False
        self.fields['country2'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country2'].label = "País 2"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"

    vaccinated = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country1 = forms.ChoiceField()
    country2 = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case15ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case15ParametersForm, self).__init__(*args, **kwargs)
        self.fields['infected'].required = False
        self.fields['infected'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['infected'].label = "Casos activos"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['department_param'].required = False
        self.fields['department_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['department_param'].label = "Parametro departamento"
        self.fields['department'].required = False
        self.fields['department'] = forms.CharField(max_length=120)
        self.fields['department'].label = "Departamento"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"
    infected = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    department_param = forms.ChoiceField()
    department = forms.CharField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case19ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case19ParametersForm, self).__init__(*args, **kwargs)
        self.fields['deaths'].required = False
        self.fields['deaths'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['deaths'].label = "Muertes"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"
    deaths = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    degree_number = forms.ChoiceField()

class Case24ParametersForm(forms.Form):
    def __init__(self, parameter_choices, countries, *args, **kwargs):
        super(Case24ParametersForm, self).__init__(*args, **kwargs)
        self.fields['infected'].required = False
        self.fields['infected'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['infected'].label = "Casos"
        self.fields['country_param'].required = False
        self.fields['country_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['country_param'].label = "Parametro país"
        self.fields['country'].required = False
        self.fields['country'] = forms.ChoiceField(choices=tuple([(param, param) for param in countries]))
        self.fields['country'].label = "País"
        self.fields['tests_param'].required = False
        self.fields['tests_param'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['tests_param'].label = "Parametro pruebas de COVID19"
        self.fields['days_to_predict'].required = False
        self.fields['days_to_predict'] = forms.CharField(max_length=10)
        self.fields['days_to_predict'].label = "Días a predecir"
        self.fields['degree_number'].required = False
        self.fields['degree_number'] = forms.ChoiceField(choices=tuple([(param, param) for param in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
        self.fields['degree_number'].label = "Grado polinomial"

    infected = forms.ChoiceField()
    country_param = forms.ChoiceField()
    country = forms.ChoiceField()
    tests_param = forms.ChoiceField()
    days_to_predict = forms.CharField()
    degree_number = forms.ChoiceField()

class Case25ParametersForm(forms.Form):
    def __init__(self, parameter_choices, *args, **kwargs):
        super(Case25ParametersForm, self).__init__(*args, **kwargs)
        self.fields['cases'].required = False
        self.fields['cases'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['cases'].label = "Parametro casos"
        self.fields['date'].required = False
        self.fields['date'] = forms.ChoiceField(choices=tuple([(param, param) for param in parameter_choices]))
        self.fields['date'].label = "Fechas"
    cases = forms.ChoiceField()
    date = forms.ChoiceField()
