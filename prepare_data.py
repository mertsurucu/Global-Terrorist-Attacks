import numpy as np
import pandas as pd
# read data from .csv file
np.set_printoptions(threshold=np.nan)
terror = pd.read_csv('GTD.csv', encoding='ISO-8859-1', usecols=[1, 2, 3, 8, 35, 58, 84, 100, 103])
terror.rename(
    columns={'eventid': 'ID', 'iyear': 'Year', 'imonth': 'Month', 'iday': 'Day', 'country_txt': 'Country',
             'region_txt': 'Region',
             'attacktype1_txt': 'AttackType', 'target1': 'Target', 'nkillter': 'Killed', 'nwoundte': 'Wounded',
             'summary': 'Summary', 'gname': 'Group', 'targtype1_txt': 'Target_type', 'weapsubtype1_txt': 'Weapon_type',
             'motive': 'Motive'}, inplace=True)
train_data = np.array([])
train_data_label = np.array([])

test_data = np.array([])
test_data_label = np.array([])

all_groups = []

for i in range(int(len(terror['Group']))):
    if terror['Group'][i] == 'Unknown': # Unknown terror attacks into test .npy
        each_row = []
        label = []
        each_row.append(terror['Year'][i])
        each_row.append(terror['Month'][i])
        each_row.append(terror['Day'][i])
        each_row.append(terror['Country'][i])
        each_row.append(terror['Target_type'][i])
        label.append(terror['Group'][i])
        each_row.append(terror['Weapon_type'][i])
        each_row.append(terror['Killed'][i])
        each_row.append(terror['Wounded'][i])
        each_row = np.array(each_row)
        test_data = np.append(test_data, each_row)
        test_data_label = np.append(test_data_label, label)
    else:
        if terror['Group'][i] not in all_groups:
            all_groups.append(terror['Group'][i])
        each_row = []
        label = []
        each_row.append(terror['Year'][i])
        each_row.append(terror['Month'][i])
        each_row.append(terror['Day'][i])
        each_row.append(terror['Country'][i])
        each_row.append(terror['Target_type'][i])
        label.append(terror['Group'][i])
        each_row.append(terror['Weapon_type'][i])
        each_row.append(terror['Killed'][i])
        each_row.append(terror['Wounded'][i])
        each_row = np.array(each_row)
        train_data = np.append(train_data, each_row)
        train_data_label = np.append(train_data_label, label)




