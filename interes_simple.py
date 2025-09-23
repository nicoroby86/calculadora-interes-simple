# day_2_interes_simple.py


# Interes SIMPLE

capital = 2000     # capital inicial
tasa = 0.08        # 8% de porcentaje anual  
tiempo = 5         # 5 anos

# Formula interes SIMPLE: P * (1 + r * t)
monto_final = capital * (1 + tasa * tiempo)

print(f'''
Calculo Interes SIMPLE
----------------------
Capital inicial: ${capital}
Tasa anual: {tasa:.0%}
Tiempo: {tiempo} anos
Monto final: ${monto_final:.2f}
----------------------
Calculo Interes SIMPLE
----------------------
''')
