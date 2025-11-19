import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("📊 Анализ чаевых в ресторане")

# Загрузка данных
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(url)

# Показываем данные
st.subheader("Данные о чаевых")
st.write(tips.head(10))

# Основная статистика
st.subheader("Основная статистика")
col1, col2, col3 = st.columns(3)
col1.metric("Всего записей", len(tips))
col2.metric("Средний чек", f"${tips['total_bill'].mean():.2f}")
col3.metric("Средние чаевые", f"${tips['tip'].mean():.2f}")

# Визуализации
st.subheader("Графики")

# 1. Распределение чаевых
fig, ax = plt.subplots()
sns.histplot(tips['tip'], bins=15, ax=ax)
ax.set_title('Распределение чаевых')
st.pyplot(fig)

# 2. Зависимость чаевых от счета
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)
ax.set_title('Чаевые vs Сумма счета')
st.pyplot(fig)

# 3. Чаевые по дням недели
fig, ax = plt.subplots()
sns.boxplot(data=tips, x='day', y='tip', ax=ax)
ax.set_title('Чаевые по дням недели')
st.pyplot(fig)

# 4. Чаевые по времени
fig, ax = plt.subplots()
sns.boxplot(data=tips, x='time', y='tip', ax=ax)
ax.set_title('Чаевые по времени дня')
st.pyplot(fig)