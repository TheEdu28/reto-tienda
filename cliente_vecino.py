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
respuesta = stub.TotalCarrito(carrito_pb2.CarritoRequest(usuario="ana"))
print(f"Usuario: {respuesta.usuario}")
print(f"Total en centavos: {respuesta.total_centavos}")
print(f"Artículos: {respuesta.articulos}")

print("=== Parte 2 · TotalCarrito con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.
try:
	stub.TotalCarrito(carrito_pb2.CarritoRequest(usuario="pedro"))
except grpc.RpcError as e:
	print(f"Código: {e.code()}")
	print(f"Detalles: {e.details()}")

print("=== Parte 3 · VerArticulos (streaming) ===")
# TODO: recorre stub.VerArticulos(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
try:
	articulos = stub.VerArticulos(carrito_pb2.CarritoRequest(usuario="ana"))
	for articulo in articulos:
		print(articulo)
except grpc.RpcError as e:
	print(f"Código: {e.code()}")
	print(f"Detalles: {e.details()}")
