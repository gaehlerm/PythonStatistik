import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def filtere_daten_nach_schluessel(alle_daten, schluessel, wert):
    gefilterte_daten = alle_daten[alle_daten[schluessel] == wert]
    return gefilterte_daten

def get_monat_jahr(datum_str, index):
    return int(datum_str.split('-')[index])

def fuege_monats_und_jahreszahlen_hinzu(daten):
    monat_jahr_dict = {"jahr": 0, "monat": 1}
    for monat_jahr_str, index in monat_jahr_dict.items():
        neue_daten = []
        for datum in daten['datum']:
            neue_daten.append(get_monat_jahr(datum, index))
        daten.insert(1, monat_jahr_str, neue_daten)
    # Die alte Version ist kürzer, aber gibt eine Warnung aus:
    # daten['jahr'] = daten['datum'].apply(get_jahr)

def berechne_kurven_parameter(daten, jahre, coronajahr, model_f):
    vor_corona = {}
    waehrend_corona = {}
    for jahr in jahre:
        daten_jahr = daten[daten['jahr'] == jahr]
        popt, _ = curve_fit(model_f, daten_jahr['monat'], daten_jahr['bl_tod'], p0=[3000, 0, 0, 0])
        if jahr < coronajahr:
            vor_corona[jahr] = popt
        else:
            waehrend_corona[jahr] = popt
    return vor_corona, waehrend_corona

color_sequence = ['#ff0000', '#ffa500', '#dddd00', '#008000', '#0000ff', '#4b0082', '#ee82ee']

def create_plot():
    plt.figure()
    plt.xlabel('Monat')
    plt.ylabel('Todesfälle')
    plt.title('Todesfälle pro Monat in Schleswig-Holstein')
    plt.grid()
    plt.xticks(range(1, 13))

def plotte_rohdaten(daten, jahre):
    for jahr in jahre:
        SH_jahr = filtere_daten_nach_schluessel(daten, "jahr", jahr)
        plt.plot(SH_jahr['monat'], SH_jahr['bl_tod'], label=jahr, color=color_sequence[jahr-2016])

def plotte_fits(vor_corona, waehrend_corona, model_f):
    alle_fit_params = vor_corona | waehrend_corona
    for jahr in alle_fit_params:
        for i in range(1, 13):
            plt.plot(i, model_f(i, *alle_fit_params[jahr]), 'o', color=color_sequence[jahr-2016])

def berechne_durchschnitt(parameters):
    durchschnitt = [0,0,0,0]
    for popt in parameters.values():
        durchschnitt += popt
    durchschnitt = durchschnitt/len(parameters)
    return durchschnitt

def plotte_durchschnittliche_fits(model_f, durchschnitt_vor, durchschnitt_waehrend):
    curve_fit_vor = [model_f(i, *durchschnitt_vor) for i in range(1, 13)]
    plt.plot(range(1, 13), curve_fit_vor, label='Durchschnitt vor Corona', color='black')
    curve_fit_waehrend = [model_f(i, *durchschnitt_waehrend) for i in range(1, 13)]
    plt.plot(range(1, 13), curve_fit_waehrend, label='Durchschnitt während Corona', color='black', linestyle='dashed')
    plt.legend()
    plt.show()

    create_plot()
    diff = [model_f(i, *(durchschnitt_waehrend-durchschnitt_vor)) for i in range(1, 13)]
    plt.plot(range(1, 13), diff, label='uebersterblichkeit', color='black', linestyle='dotted')
    plt.legend()
    plt.show()
