import pandas as pd
import matplotlib.pyplot as plt

def konvertiere_jahr_zu_datum(nobel):
    dates = []
    for date in nobel["year"]:
        dates.append(str(date) + "-11-01")
    nobel["jahr"] = pd.to_datetime(dates)

nobel = pd.read_csv("laureates.csv")
konvertiere_jahr_zu_datum(nobel)
nobel["geboren"] = pd.to_datetime(nobel["born"], errors="coerce")

nobel["alter"] = nobel["jahr"] - nobel["geboren"]
nobel["alter_tage"] = nobel["alter"].dt.days
nobel["alter_jahre"] = nobel["alter_tage"]/365.25

nobel.hist(column="alter_jahre")
plt.show() 