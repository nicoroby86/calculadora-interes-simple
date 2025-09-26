# day_3_interes_compuesto.py

# interes COMPUESTO

capital = 2000     # capital inicial
tasa = 0.1          # 5% anual (decimal)
tiempo = 8           # 5 anos

# Formula interes compuesto: M = P * (1 + r) ** t

monto_final = capital * (1 + tasa) ** tiempo

print(f'''
Calculo interes COMPUESTO
-------------------------
Capital incial: ${capital}
Tasa anual: {tasa:.0%}
Tiempo: {tiempo} anos
Monto final: ${monto_final:.2f}
-------------------------
''')
