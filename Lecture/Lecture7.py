import pandas as pd

# Assuming 'prices', 'dates', and 'bday' are defined and properly initialized

ser = pd.Series(data=prices, index=dates)

df = pd.DataFrame(data={'Close': ser, 'Bday': bday}, index=dates)
print(df)

x_ = ser.loc['2020-01-10']
print(x_)

ser2 = ser.copy()
print(ser2)

ser.loc['2020-01-02'] = 0
print(ser)

x = ser.loc[['2020-01-03', '2020-01-10']]
print(x)

x = ser.loc['2020-01-03':'2020-01-10']
print(x)

x = df.loc['2020-01-03', 'Close':]
print(x)

df2 = df.copy()

df2.rename(index={'2020-01-08': '1900-01-01'}, inplace=True)
print(df2)

x = df2.loc['2020-01-03':'2020-01-10', :]
print(x)