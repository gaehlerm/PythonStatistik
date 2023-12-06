import pandas as pd

from CoronaHelfer import *

# Dies ist ein Beispielprogramm wie man Daten zur Übersterblichkeit von Corona aus einer CSV-Datei
# ausliest und mit Hilfe von pandas, scipy und matplotlib auswertet.
# Die Auswertung der Daten wurde teilweise von Copilot ausgeführt.

# Der Code wurde so aufgeteilt, dass alle low-level Funktionen in CoronaHelfer.py stehen.
# In dieser Datei hier steht nur die high-level Logik, welche die low-level Funktionen aufruft.
# Dadurch ist der Code hier viel übersichtlicher und leichter zu lesen. Die low-level Funktionen
# müssen nur angeschaut werden, wenn man die Details verstehen möchte.

# daten von https://www.corona-daten-deutschland.de/dataset/uebersterblichkeit
alle_daten = pd.read_csv("uebersterblichkeit.csv")
SH = filtere_daten_nach_schluessel(alle_daten, schluessel="bundesland", wert="Schleswig-Holstein")
fuege_monats_und_jahreszahlen_hinzu(SH)

# https://www.askpython.com/python/examples/curve-fitting-in-python
# Die gewählte Fitfunktion ist etwas willkürlich, aber sie passt ganz gut.
# Für eine wissenschaftliche Auswertung müsste man dies natürlich begründen.
def model_f(x, a, b, c, d):
    return a + b*x + c*x**2 + d*x**3

jahre = range(2016, 2023)
coronajahr = 2020
params_vor, params_waehrend = berechne_kurven_parameter(SH, jahre, coronajahr, model_f)

create_plot()
plotte_rohdaten(SH, jahre)
plotte_fits(params_vor, params_waehrend, model_f)

durchschnitt_vor = berechne_durchschnitt(params_vor)
durchschnitt_waehrend = berechne_durchschnitt(params_waehrend)

plotte_durchschnittliche_fits(model_f, durchschnitt_vor, durchschnitt_waehrend)
