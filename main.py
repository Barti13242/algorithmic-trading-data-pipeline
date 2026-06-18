import yfinance as yf
moje_spolki = ["MSFT", "TSLA", "GOOGL", "META"]
testowane_srednie = [5, 10, 15, 20, 25, 30]
print("=== INICJACJA AUTONOMICZNEGO BOTA GIEŁDOWEGO ===")
with open("finalny_raport_bota.txt", "w", encoding="utf-8") as plik:
    plik.write("=== RESTRUKTURYZOWANY RAPORT ANALITYCZNY BI ===\n")
    plik.write("Wygenerowano automatycznie przez: Python Data Pipeline\n\n")
    for ticker in moje_spolki:
        print(f"Przetwarzam dane dla: {ticker}...")
        tabela = yf.Ticker(ticker).history(period="1y")
        ceny = tabela["Close"]
        zwrot_rynku = ceny.pct_change()
        najlepsze_okno = 20
        najwyzszy_zysk = -999999
        for okno in testowane_srednie:
            sma = ceny.rolling(window=okno).mean()
            sygnal = (ceny > sma).astype(int).shift(1)
            zwrot_strategii = zwrot_rynku * sygnal
            koncowy_zysk = (1 + zwrot_strategii).cumprod().iloc[-1] - 1
            if koncowy_zysk > najwyzszy_zysk:
                najwyzszy_zysk = koncowy_zysk
                najlepsze_okno = okno
        ostateczna_sma = ceny.rolling(window=najlepsze_okno).mean()
        dzisiejsza_cena = ceny.iloc[-1]
        dzisiejsza_sma = ostateczna_sma.iloc[-1]
        if dzisiejsza_cena > dzisiejsza_sma:
            decyzja = "KUPUJ! 📈"
        else:
            decyzja = "CZEKAJ / SPRZEDAJ 📉"
        linia_raportu = f"[{ticker}] Najlepsze okno: SMA {najlepsze_okno} (Zysk hist: {najwyzszy_zysk*100:.2f}%). Decyzja na dziś: {decyzja}\n"
        plik.write(linia_raportu)
print("=== PROCES ZAKOŃCZONY SUKCESEM! RAPORT ZAPISANY ===")
