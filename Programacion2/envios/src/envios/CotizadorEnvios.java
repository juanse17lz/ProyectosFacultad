package envios;

public class CotizadorEnvios {

    public double cotizar(double pesoKg) {
        return 1200 * pesoKg;
    }
    
    public double cotizar(double pesoKg, String destino) {
        double resultado = 0;
        switch(destino) {
            case "LOCAL" -> {
                resultado = 1200 * pesoKg;
            }
            case "NACIONAL" -> {
                resultado = (1200*pesoKg)*1.10;
            }
            case "INTERNACIONAL" -> {
                resultado = (1200*pesoKg)*1.35;
            }
        }
        return resultado;
    }
    
    public double cotizar(double pesoKg,double largo,double ancho,double alto) {
        double resultadoFinal = 0;
        double resultadoEstandar = 1200 * pesoKg;
        double pesoVolumetrico = (largo*ancho*alto) / 5000;
        double resultadoVolumetrico = 1200 * pesoVolumetrico;
        if (resultadoEstandar > resultadoVolumetrico) {
            resultadoFinal = resultadoEstandar;
        } else {
            resultadoFinal = resultadoVolumetrico;
        }
        return resultadoFinal;
    }
}
 
