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
    report15,
    report19,
    report24,
    report25,
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
    elif problem == '#15':
        report15.activecases_trend_department(df, variables, problem)
    elif problem == '#19':
        report19.death_lastday_firstyear(df, variables, problem)
    elif problem == '#24':
        report24.cases_tests_comparison_country(df, variables, problem)
    elif problem == '#25':
        report25.confirmed_cases_prediction_byday(df, variables, problem)
