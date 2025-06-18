import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
from typing import Union, Callable
import account


class SuperAccount:
    def __init__(self, name, *accounts):
        self.name = name
        children = []
        for single in accounts:
            if isinstance(single, account.Account):
                children.append(single)
                print(f"{single.name}, is a valid account, {len(children) - 1}th child of {name}")
