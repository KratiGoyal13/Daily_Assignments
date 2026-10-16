import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

df=pd.read_csv("urban_mobility.csv")
print("First Five rows are:")
print(df.head())

df["Energy_Per_Km"] = df["Energy_Used_kWh"] / df["Distance_Km"]
print("Energy Per Km:")
print(df[["Energy_Per_Km","Distance_Km","Energy_Per_Km"]])

print("Electric Van records:")
print(df[(df["Vehicle_Type"]=="Electric Van")&(df["Maintenance_Flag"]=="Yes")])

print("average Distance_Km and total Trips_Count:")
result=df.groupby("Vehicle_Type").agg(Average_Distance_Km=("Distance_Km","mean"),TotalTrips_Count=("Trips_Count","sum"))
print(result)

energy=df["Energy_Used_kWh"].dropna().to_numpy()
print("Energy Statistics:")
print("Mean:",np.mean(energy))
print("Max:",np.max(energy))
print("Min:",np.min(energy))

avg_energy=df.groupby("Vehicle_Type")["Energy_Used_kWh"].mean()

avg_energy.plot(kind="bar")
plt.title("Average Energy per vehicle")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Energy per vehicle")
plt.show()

with open("equipment_events.json",'r') as f:
    equipment_events=json.load(f)
print("event_id, asset type, site and severity:")
for event in equipment_events:
    event_id=event["event_id"]
    asset_type=event["asset"]
    severity=event["severity"]
    print("event_id:",event_id)
    print("asset:",asset_type)
    print("severity:",severity)

print("Records with temp above 70:")
for event in equipment_events:
    if event.get("temperature",0)>70:
        print(event)

with open("coastal_monitoring_log.txt","r") as f:
    text=f.read()
words=text.split()
print("Total words count:",len(words))

print("No of times inspection appears",text.lower().split().count("inspection"))

print("Matching lines:")
with open("coastal_monitoring_log.txt","r") as f:
    for line in f:
        if any(word in line.lower() for word in ['boardwalk', 'maintenance', 'wind']):
            print(line.strip())

