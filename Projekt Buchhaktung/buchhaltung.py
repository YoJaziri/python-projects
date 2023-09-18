import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



budget = pd.read_csv('budget-230215-155146.csv', sep= ";")
print(budget.head())
budget.info()
print(budget.shape)


out = list(budget["Out"])
iin = list(budget["In"])

summe_3_out = out[-1] +  out[-2] + out[-3]
summe_3_iin = iin[-1] +  iin[-2] + iin[-3]

print(f'{summe_3_out: .2f}')
print(f'{summe_3_iin: .2f}')

summe_out = sum(out)
summe_in = sum(iin)

gespart = summe_in - summe_out
print(f'{gespart: .2f}'),


unique_categoriy = list(budget["Category"].unique())
# print(unique_categoriy)
# print(type(unique_categoriy))

unique_categoriy_df_list = ["Category", "Sum_Out"]
unique_categoriy_df = pd.DataFrame(columns = unique_categoriy_df_list)

for category in unique_categoriy:
    x = budget[budget["Category"] == category]
    print(x)
    out_category = list(x["Out"])
    sum_out_category = sum(out_category)
    print(f'Out von {category} = {sum_out_category} Euro')
    new_row = {"Category": category, "Sum_Out" : sum_out_category}
    unique_categoriy_df = unique_categoriy_df.append(new_row, ignore_index=True)
    

print (unique_categoriy_df)

index_max = unique_categoriy_df["Sum_Out"].idxmax()
print(index_max)


meiste_geld = unique_categoriy_df.iloc[index_max, 1]
meiste_category = unique_categoriy_df.iloc[index_max, 0]

print(f'\nMario und Laura geben am meisten Geld für "{meiste_category}" in Wert von {meiste_geld} Euro aus.')



sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})


sns_plot = sns.barplot(data = unique_categoriy_df, x = "Category", y = "Sum_Out", hue ="Category", palette='viridis')
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=45) 
sns_plot.set_title("Ausgaben pro Kategorie")
sns_plot.set_xlabel("Höhe der Ausgaben")
sns_plot.set_ylabel("Kategorie")
sns_plot.figure.savefig("expenses_per_category.png", bbox_inches = 'tight')
sns_plot.figure.clf()


budget["Date"] = pd.to_datetime(budget["Date"])

print(budget)
budget.info()

budget_monaten = budget[["Date", "Out"]]
print(budget_monaten)
budget_monaten.info()

budget_monaten_grouper = budget_monaten.groupby(pd.Grouper(key ="Date",freq = "1M")).sum()
budget_monaten_grouper = budget_monaten_grouper.reset_index()
''' reset the index of Date after using grouby and sum with Date as index. Sometimes python dont reconize anymore the column of the chosen index''' 

budget_monaten_grouper['month_name'] = budget_monaten_grouper['Date'].dt.month_name()

print(budget_monaten_grouper)
budget_monaten_grouper.info()


sns_plot = sns.barplot(data = budget_monaten_grouper, x ="Out", y = "month_name", palette='viridis')
sns_plot.set_title("Plot 2")
sns_plot.set_xlabel("Date")
sns_plot.set_ylabel("Höhe")
sns_plot.figure.savefig("expenses_per_month.png", bbox_inches = 'tight')