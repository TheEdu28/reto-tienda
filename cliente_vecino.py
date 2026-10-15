# Cliente del servicio Carrito (equipo vecino) · Reto de integración
# Contrato del vecino: carrito.proto · Qué hace y con qué datos probar: servicios/carrito/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import carrito_pb2
import carrito_pb2_grpc

canal = grpc.insecure_channel("localhost:50057")
stub = carrito_pb2_grpc.CarritoStub(canal)

print("=== Parte 1 · TotalCarrito con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.TotalCarrito(...) e imprime los campos de la respuesta.

print("=== Parte 2 · TotalCarrito con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · VerArticulos (streaming) ===")
# TODO: recorre stub.VerArticulos(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
