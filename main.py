import streamlit as st
import numpy as np
import pandas as pd
import warnings

warnings.simplefilter('ignore')

st.title('株価チャート')

#st.sidebar.header('銘柄コード入力')
#code = st.sidebar.text_input('銘柄コード（4桁、半角）') + '.T'


code = st.text_input('銘柄コードを入力')
code = code + '.T'

if len(code) < 6:
    st.warning('入力お願いします')
    # 条件を満たないときは処理を停止する
    st.stop()


import pandas_datareader.data as web
import datetime

start = datetime.date(2018,1,1)
end = datetime.date.today()

#df = web.DataReader('9984.T', 'yahoo', start, end)
#st.dataframe(df)

df = web.DataReader(code, 'yahoo', start, end)


import matplotlib.pyplot as plt
import mplfinance as mpf

#fig, ax = plt.subplots()
#ax.hist(arr, bins=20)
#st.pyplot(fig)

fig = mpf.figure(figsize=(10, 10),style='yahoo')
ax1 = fig.add_subplot(1,1,1)
mpf.plot(df, ax=ax1, style='yahoo', type='candle', xrotation=30)

st.pyplot(fig)


