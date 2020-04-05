import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

class StudentData():
    def __init__(self, fnames, id_name, drop_by=None, drop_values=None):
        self.data = pd.read_csv(fnames[0])
        self.pset_averages = None
        self.id_name = id_name

        # Drop entries if user specifies
        if drop_by:
            self.data[drop_by] = self.data[drop_by].astype(str)
            strings_to_drop = list(map(lambda x: str(x), drop_values))
            self.data = self.data[~self.data[drop_by].isin(strings_to_drop)]
        self.data = self.formatter(self.data, 1)
        self.pset_averages = pd.DataFrame(index=self.data.index)
        self.pset_averages[1] = self.data.sum(axis=1)

        # Add the rest of the data
        for idx, fname in enumerate(fnames[1:]):
            new_data = pd.read_csv(fname)
            new_data = self.formatter(new_data, idx + 2)
            self.pset_averages[idx + 2] = new_data.sum(axis=1)
            self.data = self.data.merge(new_data, how="inner", left_index=True, right_index=True)

        # Normalize to max score (assumes that someone got the max score which is usually the case)
        # Does not normalize for the distribution of each problem set--this makes sense since
        # we are usually more concerned about the absolute scores of students on psets
        # We assume psets are worth the same amount
    def formatter(self, dataset, dset_num):
        self.pset_averages = self.pset_averages / self.pset_averages.max()
        self.pset_averages["total"] = self.pset_averages.sum(axis=1)
        self.pset_averages["total"] = self.pset_averages["total"] / len(fnames)
        self.data["total"] = self.pset_averages["total"]

        # Drop people with 0 overall average--likely auditors/not in class
        self.pset_averages = self.pset_averages[self.pset_averages["total"] != 0]
        self.data = self.data[self.data["total"] != 0]

    def col_formatter(self, hw_num, name):
        return str(hw_num) + "." + str(name[:3])

        # Assumes digits in name if and only if a question
        dataset.index = dataset[self.id_name]
        dataset = dataset.drop([col for col in dataset.columns if not bool(re.search(r'\d', col))], axis=1)
        dataset.columns = map(lambda x: self.col_formatter(dset_num, x), dataset.columns)
        return dataset

    def graph_average(self, threshold=1, auto_ignore=False):
        to_plot = self.pset_averages[self.pset_averages["total"] <= threshold].drop("total", axis=1)
        if auto_ignore:
            to_plot = to_plot.loc[~(to_plost[[1,2]] == 0).all()]
        if to_plot.shape[0] == 0:
            print("Threshold too low")
        else:
            ax = to_plot.T.plot()
            ax.get_legend().remove()
            ax.set_title(f"Problem Set Averages for individuals with <{threshold} overall Problem Set Scores")
            ax.set_ylabel("Problem Set Number")
            ax.set_xlabel("Percentage Score")

    def get_psets(self):
        return self.pset_averages

    def get_data(self):
        return self.data
