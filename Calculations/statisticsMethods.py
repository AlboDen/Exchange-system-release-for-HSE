import numpy as np
from numpy.polynomial import Polynomial
from pyparsing import countedArray
from scipy.integrate import quad

from scipy.stats import pearsonr
import numpy as np
from itertools import combinations
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from itertools import combinations

class Statistic:

    class OrderBookRegressions:
        regression_area_asks = None
        regression_area_bids = None

        @staticmethod
        def __bestRegression(x, y, max_degree=5, folds=5, random_state=42):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru

        @staticmethod
        def calculateRegressionNumbers(x, y):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru



        @staticmethod
        def calcSlopeLinearReg(x, y):
           pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


    class OrderBookStaticAnalisys:
        #STATIC
       		# To access the code, please contact the author lyakishev_i_vah@mail.ru
	

        #DYNAMIC
        	# To access the code, please contact the author lyakishev_i_vah@mail.ru
	

        @staticmethod
        def __countPointsInThirds(x, y):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


        @staticmethod
        def calculateParams(bidsPrice,bidsSize, asksPrice, asksSize):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


    class TimeSeriesAnalisys:
        class StandartMethods:
            class AutocorrelationResearch:
                @staticmethod
                def __getLagsWithBestCorr(timeSeries):
                    pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


                @staticmethod
                def getRelevantArrays(timeSeries):
                    pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


        class Indicators:

            @staticmethod
            def check_changesIndicator(series: np.ndarray, depth: int = 1) -> float:
                pass # To access the code, please contact the author lyakishev_i_vah@mail.ru




        @staticmethod
        def print_correlation_matrix_with_y(y_values, features_dict, y_name="y"):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru

        @staticmethod
        def _build_equation(intercept, var_names, coefs):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru

        @staticmethod
        def best_regression(y, x_dict):
            pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


    class BUILD_MODEL:
        pass # To access the code, please contact the author lyakishev_i_vah@mail.ru



