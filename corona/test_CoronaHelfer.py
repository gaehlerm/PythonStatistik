from CoronaHelfer import *

import numpy as np


def test_data_filter():
    d = {'col1': [1, 1, 2, 2], 'col2': [3, 4, 5, 6]}
    df = pd.DataFrame(data=d)
    gefilterte_daten = filtere_daten_nach_schluessel(df, 'col1', 1)
    assert gefilterte_daten['col1'].equals(pd.Series([1, 1]))

def test_get_monat_jahr():
    assert get_monat_jahr("2021-01", 0) == 2021
    assert get_monat_jahr("2021-01", 1) == 1

def test_fuege_monats_und_jahreszahlen_hinzu():
    d = {'datum': ["2021-01", "2022-02", "2021-03"]}
    df = pd.DataFrame(data=d)
    fuege_monats_und_jahreszahlen_hinzu(df)
    assert df['jahr'].equals(pd.Series([2021, 2022, 2021]))
    assert df['monat'].equals(pd.Series([1, 2, 3]))
    
def test_berechne_durchschnitt():
    params = {2020: np.array([1, 2, 3, 4]), 2021: np.array([5, 6, 7, 8])}
    assert (berechne_durchschnitt(params) == np.array([3, 4, 5, 6])).all()


