#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_pandas.py
# @time: 2018/10/11 10:18
# @desc: python 创建图表


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('2018/12/18', periods=10), columns=list('ABCD'))

df.plot()
