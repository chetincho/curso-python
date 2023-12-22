
print()
# Definimos una lista de países
campeones_del_mundo = ["Argentina", "Francia", "Alemania", "España", "Italia"]

# OPCION 1 iterando una lista
print("::: SOLUCION 1 :::")
for pais in campeones_del_mundo :
    print(pais)

print()


# OPCION 2 iteramos una lista utilizando los índices
print("::: SOLUCION 2 :::")
for indice in range(len(campeones_del_mundo)) :
    
    # Mostramos el indice y el elemento de la lista en dicha posición
    print(f"{indice} -> {campeones_del_mundo[indice]}")

print()
