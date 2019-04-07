import methods.basic
import methods.arithmetic

methods.basic.func1()
methods.arithmetic.add(1, 1)
methods.arithmetic.divide(2, 1)
methods.arithmetic.subsract(3, 1)

""" now we have a template for making functions elsewhere and using them in another script """

import pandas as pd

mjr = pd.DataFrame({'a': range(10)})
mjr.to_csv('templates/project/data/omg3.csv')