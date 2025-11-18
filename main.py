import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
#nazvanie
#opisanie
st.title('Data analysis application')
st.write('Загрузи свой Dataframe')


## shag 1 zagruzka csv 
uploaded_file = st.sidebar.file_uploader('Загрузи свой csv файл', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()
    
## shag 2 proverka 
missed_values = df.isna().sum()
missed_values = missed_values[missed_values > 0]

if len(missed_values) > 0:
    fig, ax = plt.subplot()
    sns.barplot(x=missed_values.index, y=missed_values.values)
    ax.set_title('Попуски в столбцах')
    ax.set_ylabel('колличество пропусков')
    st.pyplot(fig)
else:
    st.write("Нет пропусков ")
    st.stop()
## shag 3 zapolni  propuski
if len(missed_values) != 0:
    button = st.button('Заполнить пропуски')
    if button:
        df_filled = df[missed_values.index].copy()
        for col in df_filled.columns:
            if df_filled[col] == 'object':
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
        st.write(df_filled.head(5))
        
#shag 4       
        download_button = st.download_button(label='Скачать CSV файл',
                   data=df_filled.to_csv(),
                   file_name='filled_fate.csv')