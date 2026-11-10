"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if codigos[medio] == objetivo:
        return medio
    if objetivo < codigos[medio]:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
    return buscar_codigo(codigos, objetivo, medio + 1, derecha)

    pass


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#    a) Se encuentra el objetivo: codigos[medio] == objetivo, y se devuelve
#       medio.
#    b) El intervalo queda vacío: izquierda > derecha, lo que significa que
#       el objetivo no está, y se devuelve -1.
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#    Porque ya se comparó codigos[medio] con el objetivo y se sabe que no es
#    el objetivo (si lo fuera, la búsqueda habría terminado). Además, si se
#    dejara en el intervalo (por ejemplo, usando medio en lugar de medio - 1
#    o medio + 1), el intervalo podría no reducirse nunca (como cuando queda
#    un solo elemento) y la recursión sería infinita.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0     |    6    |   3   | 300 < 415 -> buscar a la izquierda (derecha = 2)
#       2    |     0     |    2    |   1   | 300 > 205 -> buscar a la derecha (izquierda = 2)
#       3    |     2     |    2    |   2   | 300 < 310 -> buscar a la izquierda (derecha = 1)
#       4    |     2     |    1    |   —   | izquierda > derecha -> devuelve -1
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
#En contar_desde_limite() cada llamada descarta un solo elemento (i
#    aumenta en 1), así que en el peor caso hay n llamadas. En la búsqueda
#    binaria cada llamada descarta aproximadamente la mitad de la región
#    que queda, así que se necesitan alrededor de log2(n) llamadas. El
#    progreso es lineal en un caso y logarítmico en el otro.
#


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
