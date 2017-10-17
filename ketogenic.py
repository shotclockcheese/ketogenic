import pandas as pd
import numpy as np
from operator import itemgetter

class Item:

    def __init__(self, serving_size, unit, fat, protein, carb, calories, category):
        self.serving_size = serving_size
        self.unit =unit
        self.fat = fat
        self.protein = protein
        self.carb = carb
        self.category = category
        self.calories = calories
        self.stats = np.array([fat,protein,carb,calories])

    def calculate_stats(self,portion):
        servings = portion / float(self.serving_size)
        return self.stats*servings

def summary(filename):
    diet_log = pd.read_table(filename)
    diet_log['item'] = diet_log['item'].str.replace(' ', '_')
    diet_log = diet_log.set_index('item')
    summ  = np.array(0)
    carb_dict = {}
    for item in diet_log.index:
        stats = diet.loc[item]
        globals()[item] = Item(serving_size=stats[0],unit=stats[1],fat=stats[2],protein=stats[3],carb=stats[4],calories=stats[5],category=stats[6])
        x = globals()[item].calculate_stats(diet_log.loc[item].portion)
        summ = summ + x
        if x[2] > 0:
            carb_dict[item] = x[2]
    print ""
    print "######################################"
    print "MACROS BREAKDOWN"
    print('fat: %.1f') % (summ[0])
    print('protein: %.1f') % (summ[1])
    print('carb: %.1f') % (summ[2])
    print('CALORIES: %.1f') % (summ[3]) + "\n"
    print "######################################"
    print "CARB BREAKDOWN: TOTAL = " + str(summ[2])
    for key, value in sorted(carb_dict.items(), key=itemgetter(1), reverse=True):
        print key, ": ", value
    print "######################################"



##add your own list of things keto friendly or use mine, which is basic
SPREADSHEET_PATH = "https://docs.google.com/spreadsheets/d/19zhAB--FY4WMxSVM3CTTOFhrb1hHvS5ySjru3LFaewg/export?format=tsv"

spreadsheet = pd.read_table(SPREADSHEET_PATH)
spreadsheet['item'] = spreadsheet['item'].str.replace(' ', '_')
diet = spreadsheet.set_index('item')


print "input daily log text file"
summary(raw_input("->"))