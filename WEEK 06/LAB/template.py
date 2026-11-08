"""
RECORD CHECK  -  my version
===========================

Name  : Faith George 
Lane  :  AI 
Date  : 06/11/2026

Run it:   python template.py
"""

# import modules
import pandas as pd
import matplotlib.pyplot as plt


# read data using pd.read_csv()
# .csv() created named "my_file.csv"
df = pd.read_csv("my_file.csv")   # replace with pd.read_csv("your_file.csv")


# Add a "percent" column: (value / limit) * 100.
df ["percent"]=(df["rows_loaded"]/df["rows_expected"])*100
print (df)

# add a status column using LAMBDA .apply()
df["status"] =  df["percent"].apply(
    lambda p: "OVER LIMIT" if p>=100 else "WARNING" if p>= 90 else "OK" ) 


# show only rows that are not "OK"
df["not_okay"] = df["status"]!="OK"
print (df[df["not_okay"]])

# Group data by status and print per count group
group = df.groupby("status")
print (group.value_counts())


# Save the dataframe into a new (.csv) file
df.to_csv("data_set_records.csv", index=False)


# Save one bar chart of the counts per status
df["status"].value_counts().plot(kind="bar")
plt.title("BAR CHART OF COUNTS PER STATUS.")
plt.xlabel("Status")
plt.ylabel("Value Count")
plt.savefig("status_counts_template.png")
plt.show()

# ==========================================================================

