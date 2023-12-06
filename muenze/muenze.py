import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(0)

def werfen():
    return random.randint(0, 1)

def muenze_werfen(n):
    summe = 0
    for _ in range(n):
        summe += werfen()
    return summe

def viele_muenzen(anzahl_muenzen, anzahl_wuerfe):
    resultate = []
    for i in range(anzahl_muenzen):
        resultate.append(muenze_werfen(anzahl_wuerfe))
    return resultate

def plotte_muenzwuerfe(resultate, n_muenzen, n_wuerfe, sigma):
    plt.figure()
    plt.hist(resultate, label='simulierter Münzenwurf', bins=int(6*sigma+1))
    plt.xlabel('Anzahl der Kopf-Würfe')
    plt.ylabel('Anzahl der Münzen')
    plt.title(f'Anzahl der Kopf-Würfe bei {n_muenzen} Münzen und {n_wuerfe} Würfen')
    plt.grid()

def berechne_durchschnitt(resultate):
    return sum(resultate) / len(resultate)

def berechne_standardabweichung(resultate):
    durchschnitt = berechne_durchschnitt(resultate)
    summe = 0
    for x in resultate:
        summe += (x - durchschnitt)**2
    return (summe / len(resultate))**0.5

def berechne_standardabweichung_mit_numpy(resultate):
    return np.std(resultate)

def gaussian(x, mu, sigma):
    return 1 / (sigma * (2*np.pi)**0.5) * np.exp(-0.5 * ((x - mu) / sigma)**2)

def plote_kurvenanpassung(durchschnitt, standardabweichung, n):
    d = durchschnitt
    s = standardabweichung
    x = np.linspace(d-3*s, d+3*s, 100)
    y = n*gaussian(x, d, s)
    plt.plot(x, y, label='theoretische Gauß-Kurve')
    plt.legend()
    plt.show()

n_muenzen = 100
n_wuerfe = 50
resultate = viele_muenzen(anzahl_muenzen=n_muenzen, anzahl_wuerfe=n_wuerfe)
durchschnitt = berechne_durchschnitt(resultate)
standardabweichung = berechne_standardabweichung(resultate)

plotte_muenzwuerfe(resultate, n_muenzen, n_wuerfe, standardabweichung)
plote_kurvenanpassung(durchschnitt, standardabweichung, n_muenzen)