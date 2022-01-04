from .report_models import (
    report1,
    report2,
    report4,
    report5,
    report6,
    report7,
    report8,
    report9,
    report10,
)

def resolve_problem(problem, df, variables, **kwargs):
    if problem == '#1':
        report1.infected_trend_country(df, variables, problem)
    elif problem == '#2':
        report2.infected_prediction_country(df, variables, problem)
    elif problem == '#4':
        report4.mortality_prediction_department(df, variables, problem)
    elif problem == '#5':
        report5.mortality_prediction_country(df, variables, problem)
    elif problem == '#6':
        report6.death_analysis_country(df, variables, problem)
    elif problem == '#7':
        report7.infection_trend_country_byday(df, variables, problem)
    elif problem == '#8':
        report8.infected_prediction_country_year(df, variables, problem)
    elif problem == '#9':
        report9.vaccinated_prediction_country(df, variables, problem)
    elif problem == '#10':
        report10.vaccinated_comparison_country(df, variables, problem)
