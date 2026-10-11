import threading
import time

from PIL.ImageChops import difference

from System.plugins.__TEMPLATE__ import PLUGIN_TEMPLATE
from Bets.Bets import Bets
from Calculations.statisticsMethods import Statistic
from network.BybitExchange import BybitExchange


class integralLaggedSubsystem(PLUGIN_TEMPLATE):

    def __init__(self, asset, params = [], rightToMakeBet = False):
        pass # To access the code, please contact the author lyakishev_i_vah@mail.ru




    def cecker(self):
        pass # To access the code, please contact the author lyakishev_i_vah@mail.ru


    def _runChecker(self):
        self.thread = threading.Thread(target=self.cecker, daemon=True)
        self.thread.start()

    def _stopChecker(self):
        # print("THROAT STOPED")
        self.stop_event.set()
        if self.thread and self.thread.is_alive():
            if self.inBetWaiting:
                self.thread.join()
            else:
                self.thread.join(timeout=0)

    def exo(self) -> None:
        print("EXO of an asset ", self.asset, " integralLaggedSubsystem METHOD, params: ", self.params)

    def loadBasicParams(self):
        return {
            "sensitivityLevel": BybitExchange.Klines.get_current_price(symbol=self.asset)*0.00001,
        }
    def getParams(self, viewOfOutput = None):
        """to get setted parameters"""
        if viewOfOutput == None:
            return [self.sensLevel]
        if viewOfOutput == "dict":
            return {"sensitivityLevel":self.sensLevel}