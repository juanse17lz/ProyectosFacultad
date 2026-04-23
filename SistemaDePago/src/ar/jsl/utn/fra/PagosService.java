package ar.jsl.utn.fra;

import java.math.BigDecimal;

public class PagosService {
    // API con sobrecarga
    public Recibo registrarPago(BigDecimal monto) {
        return registrarPago(monto, "EFECTIVO", "ARS");
    }
    
    public Recibo registrarPago(BigDecimal monto, String medio) {
        return registrarPago(monto,medio,"ARS");
    }
    
    public Recibo registrarPago(BigDecimal monto, String medio,String moneda) {
        BigDecimal montoSeguro = montoSeguro(monto);
        String mon = monedaSegura(moneda);
        String med = medioSeguro(medio);
        
        switch(med) {
            case "EFECTIVO":
                return procesarEfectivo(montoSeguro,mon);
            case "TARJETA":
                return procesarTarjeta(montoSeguro,mon);
            case "TRANSFERENCIA":
                return procesarTransferencia(montoSeguro,mon);
            default:
                return procesarEfectivo(montoSeguro,mon);
        }
    }
    
    private Recibo procesarEfectivo(BigDecimal monto, String moneda) {
        String detalles = "Pago en efectivo";
        return Recibo.generar(monto, moneda, "EFECTIVO", detalles);
    }
    
    private Recibo procesarTarjeta(BigDecimal monto, String moneda) {
        // Suponemos que todas las tarjetas estan autorizadas
        String autorizacion = "AUTORIZACION: Valida";
        String detalles = "Tarjeta (*****1111) 1 cuota " + autorizacion;
        return Recibo.generar(monto, moneda, "Tarjeta de Credito", detalles);
    }
    
    private Recibo procesarTransferencia(BigDecimal monto, String moneda) {
        String alias = "Sin-Alias";
        String cbuParcial = "*******";
        String detalles = "Tranferencia recibida. Alias: "+ alias + ", CBU (Parcial): " + cbuParcial;
        return Recibo.generar(monto, moneda, alias, detalles);
    }
    
    private BigDecimal montoSeguro(BigDecimal monto) {
        return (monto == null || monto.signum() <= 0 ? BigDecimal.ZERO : monto);
    }
    
    private String monedaSegura(String moneda) {
        return (moneda == null || moneda.isBlank()) ? "ARS" :moneda.toUpperCase();
    }
    
    private String medioSeguro(String medio) {
        if (medio == null) return "EFECTIVO";
        String m = medio.toUpperCase();
        if (m.equals("EFECTIVO")) return "EFECTIVO";
        if (m.equals("TARJETA") || m.equals("CREDITO") || m.equals("TC")) return "TARJETA";
        if (m.equals("TRANSFERENCIA") || m.equals("TRANFS") || m.equals("TB")) return "TRANSFERENCIA";
        return "EFECTIVO";
    }
}