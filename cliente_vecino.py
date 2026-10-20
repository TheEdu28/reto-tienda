# Cliente del servicio Carrito (equipo vecino) · Reto de integración
# Contrato del vecino: carrito.proto · Qué hace y con qué datos probar: servicios/carrito/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import carrito_pb2
import carrito_pb2_grpc

canal = grpc.insecure_channel("localhost:50057")
stub = carrito_pb2_grpc.CarritoStub(canal)

print("=== Parte 1 · TotalCarrito con un dato válido ===")
# Petición válida: usuario 'ana' registrado en el servicio
respuesta = stub.TotalCarrito(carrito_pb2.CarritoRequest(usuario="ana"))
print(f"Usuario: {respuesta.usuario}")
print(f"Total en centavos: {respuesta.total_centavos}")
print(f"Artículos: {respuesta.articulos}")

print("\n=== Parte 2 · TotalCarrito con un dato que provoca error ===")
# Petición inválida: usuario 'pedro' (o inexistente) que el servidor rechaza
try:
    stub.TotalCarrito(carrito_pb2.CarritoRequest(usuario="pedro"))
except grpc.RpcError as e:
    print(f"Código: {e.code().name}")
    print(f"Detalles: {e.details()}")

print("\n=== Parte 3 · VerArticulos (streaming) ===")
# Recorrido del stream con for
try:
    articulos = stub.VerArticulos(carrito_pb2.CarritoRequest(usuario="ana"))
    for articulo in articulos:
        print(f"Llegó artículo -> Clave: {articulo.clave} | Cantidad: {articulo.cantidad} | Subtotal: {articulo.subtotal_centavos} centavos")
except grpc.RpcError as e:
    print(f"Código: {e.code().name}")
    print(f"Detalles: {e.details()}")