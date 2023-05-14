import matplotlib.pyplot as plt

salaries = {
    1999: 284,
    2000: 314,
    2001: 352,
    2002: 393,
    2003: 430,
    2004: 466,
    2005: 516,
    2006: 601,
    2007: 725,
    2008: 825,
    2009: 784,
    2010: 792,
    2011: 839,
    2012: 887,
    2013: 949,
    2014: 1005,
    2015: 1065,
    2016: 1146,
    2017: 1221,
    2018: 1310,
    2019: 1407,
    2020: 1448,
    2021: 1548,
    2022: 1693,
}

years = list(salaries.keys())
values = list(salaries.values())

plt.plot(years, values)
plt.xlabel('Aasta')
plt.ylabel('Keskmine palk eurodes')
plt.title('Keskmise palga graafik Eestis')
plt.grid()
plt.show()
