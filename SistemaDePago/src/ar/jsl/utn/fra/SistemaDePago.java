package ar.jsl.utn.fra;

import java.math.BigDecimal;

/**
 * MedioPagoBase
 * Efectivo
 * TarjetaCredito
 * TransferenciaBancaria
 * Recibo
 * PagosService
 */
public class SistemaDePago {
    public static void main(String[] args) {
        PagosService service = new PagosService();
        
        //1) Solo monto -> por defecto EFECTIVO + ARS
        Recibo r1 = service.registrarPago(new BigDecimal("1000"));
        System.out.println(r1);
        
        Recibo r2 = service.registrarPago(new BigDecimal("15000.50"), "tarjeta");
        System.out.println(r2);
        
        Recibo r3 = service.registrarPago(new BigDecimal("5000"), "transferencia", "usd");
        System.out.println(r3);
    }    
}
