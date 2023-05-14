# region imports
from AlgorithmImports import *
# endregion

def monthly_deposit_usd(year, month):
    estonian_sal_usd = {'1999_1': 329, '1999_2': 318, '1999_3': 309, '1999_4': 303, '1999_5': 301, '1999_6': 294,
                        '1999_7': 294, '1999_8': 301, '1999_9': 298, '1999_10': 304, '1999_11': 293, '1999_12': 287,
                        '2000_1': 318, '2000_2': 308, '2000_3': 302, '2000_4': 296, '2000_5': 284, '2000_6': 298,
                        '2000_7': 294, '2000_8': 283, '2000_9': 272, '2000_10': 267, '2000_11': 268, '2000_12': 282,
                        '2001_1': 330, '2001_2': 324, '2001_3': 319, '2001_4': 314, '2001_5': 308, '2001_6': 300,
                        '2001_7': 303, '2001_8': 317, '2001_9': 321, '2001_10': 318, '2001_11': 312, '2001_12': 314,
                        '2002_1': 346, '2002_2': 342, '2002_3': 344, '2002_4': 348, '2002_5': 360, '2002_6': 375,
                        '2002_7': 390, '2002_8': 384, '2002_9': 385, '2002_10': 385, '2002_11': 393, '2002_12': 401,
                        '2003_1': 457, '2003_2': 463, '2003_3': 464, '2003_4': 467, '2003_5': 497, '2003_6': 501,
                        '2003_7': 488, '2003_8': 479, '2003_9': 484, '2003_10': 502, '2003_11': 503, '2003_12': 529,
                        '2004_1': 587, '2004_2': 588, '2004_3': 571, '2004_4': 558, '2004_5': 559, '2004_6': 566,
                        '2004_7': 571, '2004_8': 568, '2004_9': 570, '2004_10': 582, '2004_11': 605, '2004_12': 624,
                        '2005_1': 676, '2005_2': 671, '2005_3': 680, '2005_4': 667, '2005_5': 654, '2005_6': 627,
                        '2005_7': 621, '2005_8': 634, '2005_9': 631, '2005_10': 620, '2005_11': 608, '2005_12': 611,
                        '2006_1': 729, '2006_2': 717, '2006_3': 723, '2006_4': 738, '2006_5': 767, '2006_6': 760,
                        '2006_7': 762, '2006_8': 769, '2006_9': 764, '2006_10': 758, '2006_11': 774, '2006_12': 793,
                        '2007_1': 940, '2007_2': 948, '2007_3': 960, '2007_4': 980, '2007_5': 979, '2007_6': 973,
                        '2007_7': 995, '2007_8': 987, '2007_9': 1010, '2007_10': 1031, '2007_11': 1063, '2007_12': 1055,
                        '2008_1': 1215, '2008_2': 1217, '2008_3': 1281, '2008_4': 1300, '2008_5': 1282, '2008_6': 1284,
                        '2008_7': 1300, '2008_8': 1233, '2008_9': 1183, '2008_10': 1095, '2008_11': 1049, '2008_12': 1115,
                        '2009_1': 1039, '2009_2': 1003, '2009_3': 1024, '2009_4': 1034, '2009_5': 1070, '2009_6': 1098,
                        '2009_7': 1104, '2009_8': 1118, '2009_9': 1142, '2009_10': 1161, '2009_11': 1169, '2009_12': 1142,
                        '2010_1': 1129, '2010_2': 1083, '2010_3': 1074, '2010_4': 1063, '2010_5': 993, '2010_6': 966,
                        '2010_7': 1014, '2010_8': 1021, '2010_9': 1037, '2010_10': 1100, '2010_11': 1081, '2010_12': 1047,
                        '2011_1': 1122, '2011_2': 1145, '2011_3': 1176, '2011_4': 1213, '2011_5': 1201, '2011_6': 1208,
                        '2011_7': 1197, '2011_8': 1202, '2011_9': 1152, '2011_10': 1151, '2011_11': 1137, '2011_12': 1103,
                        '2012_1': 1146, '2012_2': 1173, '2012_3': 1171, '2012_4': 1167, '2012_5': 1135, '2012_6': 1112,
                        '2012_7': 1089, '2012_8': 1099, '2012_9': 1143, '2012_10': 1150, '2012_11': 1138, '2012_12': 1163,
                        '2013_1': 1262, '2013_2': 1265, '2013_3': 1230, '2013_4': 1235, '2013_5': 1231, '2013_6': 1252,
                        '2013_7': 1243, '2013_8': 1263, '2013_9': 1268, '2013_10': 1294, '2013_11': 1280, '2013_12': 1300,
                        '2014_1': 1368, '2014_2': 1373, '2014_3': 1389, '2014_4': 1387, '2014_5': 1380, '2014_6': 1366,
                        '2014_7': 1360, '2014_8': 1337, '2014_9': 1294, '2014_10': 1274, '2014_11': 1253, '2014_12': 1237,
                        '2015_1': 1236, '2015_2': 1208, '2015_3': 1153, '2015_4': 1151, '2015_5': 1189, '2015_6': 1196,
                        '2015_7': 1171, '2015_8': 1186, '2015_9': 1196, '2015_10': 1194, '2015_11': 1142, '2015_12': 1160,
                        '2016_1': 1245, '2016_2': 1272, '2016_3': 1276, '2016_4': 1299, '2016_5': 1294, '2016_6': 1288,
                        '2016_7': 1267, '2016_8': 1284, '2016_9': 1284, '2016_10': 1263, '2016_11': 1236, '2016_12': 1207,
                        '2017_1': 1298, '2017_2': 1299, '2017_3': 1304, '2017_4': 1308, '2017_5': 1350, '2017_6': 1372,
                        '2017_7': 1408, '2017_8': 1442, '2017_9': 1453, '2017_10': 1435, '2017_11': 1433, '2017_12': 1445,
                        '2018_1': 1597, '2018_2': 1616, '2018_3': 1616, '2018_4': 1608, '2018_5': 1548, '2018_6': 1529,
                        '2018_7': 1531, '2018_8': 1511, '2018_9': 1526, '2018_10': 1505, '2018_11': 1488, '2018_12': 1490,
                        '2019_1': 1606, '2019_2': 1596, '2019_3': 1590, '2019_4': 1581, '2019_5': 1574, '2019_6': 1590,
                        '2019_7': 1577, '2019_8': 1567, '2019_9': 1551, '2019_10': 1556, '2019_11': 1554, '2019_12': 1563,
                        '2020_1': 1607, '2020_2': 1580, '2020_3': 1603, '2020_4': 1573, '2020_5': 1582, '2020_6': 1629,
                        '2020_7': 1660, '2020_8': 1713, '2020_9': 1706, '2020_10': 1703, '2020_11': 1715, '2020_12': 1763,
                        '2021_1': 1883, '2021_2': 1872, '2021_3': 1842, '2021_4': 1852, '2021_5': 1880, '2021_6': 1863,
                        '2021_7': 1831, '2021_8': 1821, '2021_9': 1822, '2021_10': 1795, '2021_11': 1765, '2021_12': 1750,
                        '2022_1': 1916, '2022_2': 1920, '2022_3': 1864, '2022_4': 1829, '2022_5': 1791, '2022_6': 1788,
                        '2022_7': 1725, '2022_8': 1713, '2022_9': 1678, '2022_10': 1665, '2022_11': 1731, '2022_12': 1792,
                        '2023_1': 1792}
    percentage = 0.1
    keyidx = f'{year}_{month}'
    return int(estonian_sal_usd[keyidx] * percentage)

class Rebalance(QCAlgorithm):
    def Initialize(self):
        # self.SetAccountCurrency("USD")

        self.start_year = 2000
        self.SetStartDate(self.start_year, 1, 1)
        self.SetEndDate(2023, 2, 1)

        self.spy = self.AddEquity("SPY", Resolution.Daily)

        deposit = monthly_deposit_usd(self.start_year, self.Time.month)
        self.SetCash(deposit)
        self.invested = 0
        self.invested += deposit

        # self.SetWarmUp(timedelta(days=100), Resolution.Daily)
        self.Schedule.On(self.DateRules.MonthStart(3),
                         self.TimeRules.At(10, 0), self.MonthlyDeposit)

        self.Schedule.On(self.DateRules.MonthStart(4),
                         self.TimeRules.At(10, 0), self.QuarterlyInvest)

        self.Schedule.On(self.DateRules.MonthEnd(),
                         self.TimeRules.At(10, 0), self.StatsPrint)

    def MonthlyDeposit(self):
        year = self.Time.year
        if year < self.start_year:
            return

        if not (year == self.start_year and self.Time.month == 1):
            deposit = monthly_deposit_usd(year, self.Time.month)
            self.Portfolio.CashBook["USD"].AddAmount(deposit)
            self.invested += deposit

        self.Plot("Strategy Equity", "Amount Inv", self.invested)
    
    def QuarterlyInvest(self):
        if self.Time.month % 3 != 0:
            return

        year = self.Time.year
        if year < self.start_year:
            return
        
        free_cash = self.Portfolio.CashBook["USD"].Amount
        buypower = free_cash / self.spy.Close

        if buypower < 1:
            return
 
        self.SetHoldings(self.spy.Symbol, 0.5)

    def StatsPrint(self):
        year = self.Time.year
        t = str(year) + "-" + str(self.Time.month) + \
            "-" + str(self.Time.day)

        free_cash = self.Portfolio.CashBook["USD"].Amount

        profit = self.Portfolio["SPY"].TotalCloseProfit()
        eq1 = self.Portfolio["SPY"].HoldingsValue
        cash_invested = self.invested
        eq_all = eq1 + free_cash
        roi = ((eq_all / cash_invested) - 1) * 100 if eq1 != 0 and cash_invested != 0 else 0 

        self.Plot("Return on investment", "ROI", roi)

        self.Debug(t +
                   " invested " + str(self.invested) +
                   " profit " + str(profit) +
                   " equity1 " + str(eq1) +
                   " free cash " + str(free_cash) +
                   " ROI " + str(roi))
        self.Debug(t +
                   " invested E " + str(self.invested / 1.09) +
                   " profit E " + str(profit / 1.09) +
                   " equity1 E " + str(eq1 / 1.09) +
                   " free cash E " + str(free_cash / 1.09) +
                   " eqAll E " + str(eq_all / 1.09) +
                   " ROI " + str(roi))
        self.Debug(" ")
