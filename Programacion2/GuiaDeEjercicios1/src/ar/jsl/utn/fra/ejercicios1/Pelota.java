package ar.jsl.utn.fra.ejercicios1;

public class Pelota {
    //Atributos
    private String marca;
    private double circunferencia;
    
    //Setter
    public void setCircunferencia(double unaCircunferencia) {
        circunferencia = unaCircunferencia;
    }
    public void setMarca(String unaMarca) {
        marca = unaMarca;
    }
    
    //Getter
    public double getCircunferencia() {
        return circunferencia;
    }
    public String getMarca() {
        return marca;
    }
    
    //Metodos
    public void compararCircunferencia(double circunferenciaUno, double circunferenciaDos) {
        if (circunferenciaUno == circunferenciaDos) {
            System.out.println("Las pelotas son iguales.");
        } else {
            System.out.println("Las pelotas son distintas");
        }
    }
    public void inflarPelota() {
        double radio = circunferencia / (2 * 3.1416);
        circunferencia = 2 * 3.1416 * (radio + 1);
    }
    public void desinflarPelota() {
        double radio = circunferencia / (2 * 3.1416);
        circunferencia = 2 * 3.1416 * (radio - 1);
    }
}
