import os
import pandas as pd
import numpy as np
import csv
import glob
from datetime import datetime
from csv import reader
import matplotlib.pyplot as plt
import seaborn as sns
import csv


Source = 'laptop'  # 'work' or 'laptop'

if Source == 'laptop':
    USB = 'E'
else:
    USB = 'D'
