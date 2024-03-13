
import sys

try:
    # Obtener tasas de conversión y cantidad de pesos chilenos
    tasas = [float(arg) for arg in sys.argv[1:4]]
    clp = float(sys.argv[4])

    # Realizar las conversiones
    soles = clp * tasas[0]
    pesos_argentinos = clp * tasas[1]
    usd = clp * tasas[2]

    # Imprimir resultado
    print(f"Los {clp} pesos equivalen a:")
    print(f"{soles} Soles")
    print(f"{pesos_argentinos} Pesos Argentinos")
    print(f"{usd} Dólares")

except (ValueError, IndexError):
    print("Formato invalido, debe ingresar: <tasa_sol> <tasa_peso_arg> <tasa_dolar> <cantidad_pesos>")
    sys.exit(1)
