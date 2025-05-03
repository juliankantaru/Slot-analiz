import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri
data = {
    'slot_name': ['Book of Ra'] * 5 + ['Sweet Bonanza'] * 5,
    'bet': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    'win': [0, 5, 0, 0, 3, 0, 0, 10, 0, 0],
    'timestamp': pd.date_range(start='2025-05-01 15:00', periods=10, freq='2min')
}
df = pd.DataFrame(data)

# Başlık
st.title("Slot Oyunu Analiz Paneli")

# Slot seçimi
selected_slot = st.selectbox("Bir slot oyunu seç:", df['slot_name'].unique())

# Seçilen slot için filtreleme
slot_df = df[df['slot_name'] == selected_slot]

# Hesaplamalar
total_bet = slot_df['bet'].sum()
total_win = slot_df['win'].sum()
rtp = total_win / total_bet if total_bet != 0 else 0
volatility = slot_df['win'].std()
average_win = slot_df['win'].mean()

# Sonuçlar
st.subheader(f"{selected_slot} İstatistikleri")
st.write(f"Toplam Bahis: {total_bet}")
st.write(f"Toplam Kazanç: {total_win}")
st.write(f"RTP (Oyuncuya Dönüş Oranı): {rtp:.2f}")
st.write(f"Volatilite (Standart Sapma): {volatility:.2f}")
st.write(f"Ortalama Kazanç: {average_win:.2f}")

# Grafik
st.subheader("Kazanç Zaman Grafiği")
fig, ax = plt.subplots()
ax.plot(slot_df['timestamp'], slot_df['win'], marker='o', linestyle='-')
ax.set_title(f"{selected_slot} Kazanç Zaman Çizgisi")
ax.set_xlabel("Zaman")
ax.set_ylabel("Kazanç")
st.pyplot(fig)