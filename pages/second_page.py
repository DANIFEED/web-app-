import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

st.title("📈 Котировки Apple (AAPL)")

# Параметры дат
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Начальная дата", value=pd.to_datetime("2023-01-01"))
with col2:
    end_date = st.date_input("Конечная дата", value=pd.to_datetime("2024-01-01"))

# Кнопка загрузки
if st.button("Загрузить данные"):
    # Загрузка данных
    apple_data = yf.download("AAPL", start=start_date, end=end_date)
    
    if not apple_data.empty:
        st.success("Данные успешно загружены!")
        
        # Преобразуем все в числа
        start_price = float(apple_data['Close'].iloc[0])
        end_price = float(apple_data['Close'].iloc[-1])
        max_price = float(apple_data['Close'].max())
        min_price = float(apple_data['Close'].min())
        avg_price = float(apple_data['Close'].mean())
        
        # Основная информация
        st.subheader("Основная информация")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Начальная цена", f"${start_price:.2f}")
        col2.metric("Конечная цена", f"${end_price:.2f}")
        change = ((end_price - start_price) / start_price) * 100
        col3.metric("Изменение", f"{change:.2f}%")
        col4.metric("Максимальная цена", f"${max_price:.2f}")
        
        # Показываем последние данные
        st.subheader("Последние 5 дней")
        st.write(apple_data.tail())
        
        # График цен закрытия
        st.subheader("График цен закрытия")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(apple_data.index, apple_data['Close'], linewidth=2)
        ax.set_title('Цены закрытия Apple (AAPL)')
        ax.set_ylabel('Цена ($)')
        ax.set_xlabel('Дата')
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # График объемов
        st.subheader("Объемы торгов")
        fig, ax = plt.subplots(figsize=(12, 4))
        
        # Преобразуем объемы в миллионы для лучшего отображения
        volumes_millions = apple_data['Volume'] / 1_000_000
        ax.plot(apple_data.index, volumes_millions, color='orange', alpha=0.7)
        ax.set_title('Объемы торгов (в миллионах)')
        ax.set_ylabel('Объем (млн)')
        ax.set_xlabel('Дата')
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # Дополнительная информация
        st.subheader("Дополнительная статистика")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Минимальная цена:** ${min_price:.2f}")
            st.write(f"**Средняя цена:** ${avg_price:.2f}")
            
        with col2:
            st.write(f"**Всего торговых дней:** {len(apple_data)}")
            st.write(f"**Период:** {start_date} - {end_date}")
        
    else:
        st.error("Не удалось загрузить данные")
else:
    st.info("Нажмите кнопку 'Загрузить данные' для получения котировок Apple")