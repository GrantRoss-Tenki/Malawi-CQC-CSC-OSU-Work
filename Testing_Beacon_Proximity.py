import itertools
import os
import pandas as pd
import numpy as np
import csv
from decimal import *
from itertools import chain
import statistics as stat
import datetime
from datetime import datetime
from itertools import islice, cycle
from io import StringIO
import matplotlib.pyplot as plt
import Functions_malawi


Source = 'work' #input("laptop or Work: ")  # 'work' or 'laptop'

if Source == 'laptop':
    USB_D = 'D'
elif Source != 'laptop':
    USB_D = 'F'


Beacon_tester_array = USB_D+":/Malawi 1.1/Proximity_tester_array.csv"
Array = pd.read_csv(Beacon_tester_array)
