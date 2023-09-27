import yfinance as yf
from django.shortcuts import render
from .forms import BitcoinProfitForm

# Vista para calcular las ganancias de Bitcoin
def calculate_profit(request):
    if request.method == 'POST':
        form = BitcoinProfitForm(request.POST)
        if form.is_valid():
            irrupto_selector = form.cleaned_data['irrupto_selector']
            period = form.cleaned_data['period']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Descargar datos históricos de Bitcoin usando yfinance
            data = yf.download(irrupto_selector, start=start_date, end=end_date)

            # Verificar si hay datos disponibles
            if not data.empty:
                # Calcular ganancias
                buy_price = data['Open'][0]
                sell_price = data['Close'][-1]
                profit = (sell_price - buy_price) / buy_price * 100
            else:
                # No hay datos disponibles para el período especificado
                profit = None

            # Renderizar el resultado en la plantilla
            return render(request, 'bitcoin_app/calculate_profit.html', {'form': form, 'profit': profit})

    else:
        form = BitcoinProfitForm()

    return render(request, 'bitcoin_app/calculate_profit.html', {'form': form})

