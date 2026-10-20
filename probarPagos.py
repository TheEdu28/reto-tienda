import grpc

import pagos_pb2
import pagos_pb2_grpc

# Conexión al servidor local de Pagos en el puerto 50056
canal = grpc.insecure_channel("localhost:50056")
stub = pagos_pb2_grpc.PagosStub(canal)

print("=== Prueba 1: Especificando metodo='oxxo' ===")
peticion_oxxo = pagos_pb2.CobroRequest(
    pedido="PED-100", 
    monto_centavos=50000, 
    metodo="oxxo"
)
for p in stub.SeguirCobro(peticion_oxxo):
    print(f"Paso {p.numero}: {p.paso}")

print("\n=== Prueba 2: Sin especificar metodo (debe tomar el default 'tarjeta') ===")
peticion_default = pagos_pb2.CobroRequest(
    pedido="PED-100", 
    monto_centavos=50000
)
for p in stub.SeguirCobro(peticion_default):
    print(f"Paso {p.numero}: {p.paso}")