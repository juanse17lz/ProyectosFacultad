package ar.jsl.utn.fra;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public class Recibo {
    public static int contadorDeInstancia = 0;
    private int id;
    private LocalDateTime fecha;
    private BigDecimal monto;
    private String moneda;
    private String medioPago;
    private String detalles;

    public Recibo(LocalDateTime fecha, BigDecimal monto, String moneda, String medioPago, String detalles) {
        contadorDeInstancia++;
        this.id = contadorDeInstancia;
        this.fecha = fecha;
        this.monto = monto;
        this.moneda = moneda;
        this.medioPago = medioPago;
        this.detalles = detalles;
    }
    
    public static Recibo generar(BigDecimal monto,String moneda, String medioPago, String detalles) {
        return new Recibo(
                LocalDateTime.now(),
                monto,
                moneda,
                medioPago,
                detalles
        );
    }
    
    @Override
    public String toString() {
        return "----------Recibo----------\n"
               +"id: "+ id +"\n"
               +"Fecha: " + fecha + "\n"
               +"Monto: " + monto.toPlainString() + "\n"
               +"Moneda: " + moneda + "\n"
               +"Medio de pago: " + medioPago + "\n"
               +"Detalles: " + detalles + "\n"; 
    }
}
