import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

spolki = ['MSFT', 'TSLA', 'GOOGL', 'META']
print("=== INICJACJA AUTONOMICZNEGO BOTA GIEŁDOWEGO Z SYGNAŁAMI ===")

for ticker in spolki:
    print(f"\nPrzetwarzam dane dla: {ticker}...")
    dane = yf.download(ticker, period="3m", interval="1d")
    
    if dane.empty:
        print(f"Brak danych dla {ticker}")
        continue
    
    # Naprawa struktury danych dla nowej wersji yfinance
    if isinstance(dane.columns, pd.MultiIndex):
        dane.columns = dane.columns.droplevel(1)
        
    # Obliczanie średnich kroczących
    dane['SMA5'] = dane['Close'].rolling(window=5).mean()
    dane['SMA20'] = dane['Close'].rolling(window=20).mean()
    
    ostatni_dzien = dane.iloc[-1]
    cena_zamkniecia = float(ostatni_dzien['Close'])
    sma5 = float(ostatni_dzien['SMA5'])
    sma20 = float(ostatni_dzien['SMA20'])
    
    if sma5 > sma20:
        rekomendacja = "KUPUJ"
        znacznik = "🟢"
    elif sma5 < sma20:
        rekomendacja = "SPRZEDAJ"
        znacznik = "🔴"
    else:
        rekomendacja = "CZEKAJ"
        znacznik = "🟡"
        
    print(f"Aktualna cena {ticker}: {cena_zamkniecia:.2f} USD")
    print(f"Rekomendacja bota: {znacznik} {rekomendacja}")
    
    # Rysowanie i wymuszenie zapisu wykresu
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(dane.index, dane['Close'], label='Cena', color='blue')
        plt.plot(dane.index, dane['SMA5'], label='SMA 5', color='orange')
        plt.plot(dane.index, dane['SMA20'], label='SMA 20', color='red')
        plt.title(f"{ticker} - {rekomendacja}")
        plt.grid(True)
        plt.legend()
        
        # Zapis bezpośrednio do głównego folderu bota
        sciezka_wykresu = f"C:/BotGieldowy/wykres_{ticker}.png"
        plt.savefig(sciezka_wykresu, bbox_inches='tight')
        plt.close()
        print(f"Sukces! Wykres zapisany w: {sciezka_wykresu}")
    except Exception as e:
        print(f"Błąd podczas tworzenia wykresu dla {ticker}: {e}")

print("\n=== PROCES ZAKOŃCZONY! SPRAWDŹ FOLDER C:/BotGieldowy ===")
