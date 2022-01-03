import matplotlib.pyplot as plt
from .reports import (
    mortality_prediction_country,
    death_analysis_country
)

def resolve_problem(problem, df, variables, **kwargs):
    if problem == '#1':
        pass
    elif problem == '#2':
        pass
    elif problem == '#6':
        return death_analysis_country(df, variables, problem)
