#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

from pathlib import Path
import numpy as np
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
np.random.seed(42)

path = Path('transcripts', 'parsed')

files = path.glob(('**/content.csv'))
words = sum(
    pd.read_csv(file).content.str.split().str.len().sum() for file in files
)
print(words)

# print(len(list(files)))
