# Nuestro equipo

- **Nuestro servicio:** Pagos · puerto 50056 · contrato `pagos.proto`
- **Servicio que consumimos (vecino):** Carrito · puerto 50057 · contrato `carrito.proto`
- **Repositorio del equipo vecino:** https://github.com/Angelk234/reto-tienda_carrito

| Integrante | Matrícula | Rol |
|---|---|---|
| Jesus Eduardo Lazo | 20212702 | Servidor |
|   Ethan Jose Carbajal Guzman | 20207889 | Cliente |
| Estefhany Maribel Torres Oseguera | 20204626 | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
=== Parte 1 · TotalCarrito con un dato válido ===
Usuario: ana
Total en centavos: 1329800
Artículos: 2
=== Parte 2 · TotalCarrito con un dato que provoca error ===
Código: StatusCode.NOT_FOUND
Detalles: El usuario no tiene carrito
=== Parte 3 · VerArticulos (streaming) ===
Código: StatusCode.UNKNOWN
Detalles: Exception iterating responses: module 'carrito_pb2' has no attribute 'Articulos'
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

¿Usaron IA? ¿Cuál, quién y para qué? (por ejemplo: "Copilot para el for de la parte 3; lo revisamos línea por línea").

- Copilot para corregir de la función SeguirCobro y revisamos lo que nos dió.
