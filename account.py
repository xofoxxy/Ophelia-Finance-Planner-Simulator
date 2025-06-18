import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
from typing import Union, Callable

class Account:
    def __init__(self, name, *, balance=0, income=0, costs=0, appreciation=0):
        self.name = name
        self.balance = balance
        self.appreciation = appreciation
        self.balance_history = pd.DataFrame()
        
        # Handle costs: convert constants to functions, keep functions as is
        if callable(costs):
            self.costs = costs
            self.costs_name = costs.__name__
        else:
            self.costs = lambda t: costs
            self.costs_name = 'costs'
            
        # Handle income: convert constants to functions, keep functions as is
        if callable(income):
            self.income = income
            self.income_name = income.__name__
        else:
            self.income = lambda t: income
            self.income_name = 'income'

    def simple_project_balance(self, years):
        def aggregate(func, name, years):
            years = int(years)
            time_points = np.linspace(0, years, num=years*12 + 1)  # monthly points plus endpoint
            
            if callable(func):
                # Evaluate the function at all time points
                values = [func(t) for t in time_points]
                # Calculate cumulative integral
                partial_aggregates = sp.integrate.cumulative_trapezoid(values, time_points)
                
                # Store yearly values
                for year in range(years+1):
                    year_idx = (year + 1)  # +1 because cumulative_trapezoid returns one less point
                    #print(f"{self.name}'s {name} aggregate in {year} years from now is {partial_aggregates[year_idx]}")
                    
                    if name not in self.balance_history.columns:
                        self.balance_history[name] = 0
                    self.balance_history.loc[year, name] = partial_aggregates[year_idx]
            else:
                # Handle constant values
                for year in range(years):
                    partial_aggregate = year * func
                    #print(f"{self.name}'s {name} aggregate is {partial_aggregate}")
                    
                    if name not in self.balance_history.columns:
                        self.balance_history[name] = 0
                    self.balance_history.loc[year, name] = partial_aggregate

        # Initialize DataFrame with enough rows
        self.balance_history = pd.DataFrame(index=range(years))
        
        # Aggregate costs and income
        aggregate(self.costs, self.costs_name, years)
        aggregate(self.income, self.income_name, years)
        
        # Initialize balance column
        if 'balance' not in self.balance_history.columns:
            self.balance_history['balance'] = 0
            self.balance_history.loc[0, 'balance'] = self.balance
        
        # Calculate balance progression
        for year in range(1, years):
            self.balance_history.loc[year, 'balance'] = (
                self.balance_history.loc[year-1, 'balance'] * self.appreciation +
                self.balance_history.loc[year-1, self.income_name] -
                self.balance_history.loc[year-1, self.costs_name]
            )

        print(f"{self.name}'s balance aggregate is {self.balance_history.loc[years-1, 'balance']}")
        return self.balance_history.loc[years-1, 'balance']

    def graph_everything(self):
        figure, axis = plt.subplots(len(self.balance_history.columns), sharex=True)
        for column in self.balance_history.columns:
            print(column)
            column_idx = self.balance_history.columns.get_loc(column)
            print(column_idx)
            axis[column_idx].set_title(column)

            axis[column_idx].plot(self.balance_history.index+1,self.balance_history[column])
        plt.tight_layout()
        plt.show()