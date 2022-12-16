import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
d_parser=lambda x:pd.datetime.strptime(x,'%Y%m%d-%H:%M')
df1=pd.read_csv('testset1.csv',parse_dates=['datetime_utc'],date_parser=d_parser)

df1=df1[['datetime_utc','_tempm']]
df1['datetime_utc'] = pd.to_datetime(df1['datetime_utc']).dt.date
df1['datetime_utc']=pd.to_datetime(df1['datetime_utc'])
df1['year'] = df1['datetime_utc'].dt.year
max_temp = df1.groupby('year')['_tempm'].max()
delhi=pd.DataFrame(max_temp)
delhi.reset_index(inplace=True)

bombay=pd.read_csv('bombay.csv')
bombay=bombay[['Year','Temp']]
filt= (bombay['Year']>=1996) & (bombay['Year']<=2017)
bombay=bombay[filt]
max_temp_bom=bombay.groupby('Year')['Temp'].max()
bombay_new=pd.DataFrame(max_temp_bom)
bombay_new.reset_index(inplace=True)

plt.figure(figsize=(8, 6), dpi=80)
sns.set_style('darkgrid')
plt.plot(delhi['year'], delhi['_tempm'], label='Delhi Temperature', marker='.',color='#0343DF')
plt.plot(bombay_new['Year'], bombay_new['Temp'], label='Bombay Temperature', marker='.', color='#DC143C')
plt.title('Temperature(Winters) vs Year',fontsize=20)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Temperature(F)',fontsize=15)
plt.legend()
plt.tight_layout()
