import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

st.title("Saham Perusahaan Indonesia")

saham_indonesia = {
    'BBRI.JK': 'Bank Rakyat Indonesia',
    'BBCA.JK': 'Bank Central Asia',
    'BMRI.JK': 'Bank Mandiri',
    'BBTN.JK': 'Bank Tabungan Negara',
    'TLKM.JK': 'Telkom Indonesia',
}

nama_perusahaan = st.sidebar.selectbox("Pilih Perusahaan", list(saham_indonesia.values()))
ticker = [kode for kode, nama in saham_indonesia.items() if nama == nama_perusahaan][0]

current_year = datetime.date.today().year
start_date = st.sidebar.date_input("Pilih Tanggal Mulai", datetime.date(current_year, 1, 1))
end_date = st.sidebar.date_input("Pilih Tanggal Selesai", datetime.date.today())

if st.sidebar.button("Ambil Data Saham"):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        st.subheader(f"Data Saham ({nama_perusahaan})")
        st.write(stock_data.tail())

        st.subheader(f"Grafik Harga Saham ({nama_perusahaan})")
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Close'], label='Harga Penutupan', color='#F63366')
        plt.xlabel('Tanggal')
        plt.ylabel('Harga (IDR)')
        plt.legend()
        st.pyplot(plt)

        st.subheader(f"Metrik Statistik Saham ({nama_perusahaan})")
        st.write(stock_data.describe())

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

else:
    st.info("Masukkan inputan untuk mendapatkan data saham perusahaan")
