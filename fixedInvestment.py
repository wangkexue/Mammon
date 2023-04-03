import matplotlib
import matplotlib.pyplot as plt
from pandas_datareader import get_data_yahoo

matplotlib.style.use('ggplot')
sse_compsite_index = get_data_yahoo('000001.SS')

plt.figure()
sse_compsite_index['Open'].plot()
plt.show()

class fixed_monthly_investment:
    def __init__(self, data):
        self.data = data
        

    def get_value(self):
        return self.value

    def get_annualized_rate_of_return(self):
        pass