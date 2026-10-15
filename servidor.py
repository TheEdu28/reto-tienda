# Servidor del servicio Pagos · Reto de integración · Unidad II
# Contrato: pagos.proto · Puerto: 50056
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures

import pagos_pb2
import pagos_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
PEDIDOS = {
    "PED-100": (True, 1329800),
    "PED-101": (False, 89900),
}
PASOS = ["Validando datos", "Autorizando con el banco", "Cobro aprobado"]


class PagosServicio(pagos_pb2_grpc.PagosServicer):

    def ConsultarPago(self, request, context):
        # UNARIO: regresa UNA caja con return
        # Si el pedido no existe: context.abort(grpc.StatusCode.NOT_FOUND, ...)
        # Si existe: regresa un pagos_pb2.EstadoPago con pedido, pagado y monto.
        if request.pedido not in PEDIDOS:
            context.abort(grpc.StatusCode.NOT_FOUND, "Pedido no encontrado")

        pagado, monto = PEDIDOS[request.pedido]
        return pagos_pb2.EstadoPago(
            pedido=request.pedido,
            pagado=pagado,
            monto_centavos=monto,
        )

ddef SeguirCobro(self, request, context):
        if request.monto_centavos <= 0:
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT, 
                f"El monto debe ser mayor a 0: {request.monto_centavos}"
            )

        for numero, descripcion in enumerate(PASOS, start=1):
            time.sleep(1)
            # CORRECCIÓN AQUÍ: usar 'paso=' en lugar de 'mensaje='
            yield pagos_pb2.PasoCobro(numero=numero, paso=descripcion)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pagos_pb2_grpc.add_PagosServicer_to_server(PagosServicio(), servidor)
servidor.add_insecure_port("[::]:50056")
servidor.start()
print("Servidor de Pagos escuchando en el puerto 50056...")
servidor.wait_for_termination()
