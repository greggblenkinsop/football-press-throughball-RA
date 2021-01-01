import os
import pandas as pd
import statsmodels.api as sm
import statistics
import matplotlib.pyplot as plt
import numpy as np

# create empty lists to store relevant information from each file (team)
teams_list = []
x_list = []
y_list = []
colours_list = []

# iterate through every file within the relevant directory
for filename in os.listdir("./teams"):
    if filename.endswith(".xlsx"):

        # open the excel file and declare the column names
        colnames = ['Opponent', 'Def3rd', 'Mid3rd', 'Att3rd', 'TB']
        data = pd.read_excel("./teams/" + filename, names=colnames)
        pd.options.display.max_columns = len(data.columns)

        # convert the columns of the excel file to lists
        throughballs = data.TB.tolist()
        def3rd = data.Def3rd.tolist()
        mid3rd = data.Mid3rd.tolist()
        att3rd = data.Att3rd.tolist()

        avgpos = []

        # iterate through every game to calculate the average position of the opponents press
        for x in range(len(def3rd)):

            # this process could be improved by using exact press positions in the future instead of approximating
            d3 = (def3rd[x] * (1 / 6))
            m3 = (mid3rd[x] * (1 / 2))
            a3 = (att3rd[x] * (5 / 6))
            tot = (def3rd[x] + mid3rd[x] + att3rd[x])
            presspos = (d3 + m3 + a3) / tot

            # add the calculated value to a list
            avgpos.append(presspos)

        # declare variables for the analysis
        ind_var = data[['TB']]
        dep_var = avgpos

        # running the analysis and getting the r-squared value
        x = sm.add_constant(dep_var)
        model = sm.OLS(ind_var, x).fit()
        rvalue = model.rsquared

        print(filename[:-5], ": Average press position of opposition:", statistics.mean(avgpos),
              "Average through balls completed:", statistics.mean(throughballs), " R-Value:", rvalue)

        # adding relevant data to be graphed
        x_list.append(statistics.mean(avgpos))
        y_list.append(statistics.mean(throughballs))
        teams_list.append(filename[:-5])
        colours_list.append(rvalue)

        continue
    else:
        continue


# creating the graph
plt.scatter(np.array(x_list), np.array(y_list), c=np.array(colours_list))

for x_pos, y_pos, team in zip(x_list, y_list, teams_list):
    plt.annotate(team, xy=(x_pos, y_pos))

plt.xlabel("The average position of a press from the opponent team")
plt.ylabel("The average amount of through balls by the target team")
plt.show()
