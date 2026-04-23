package ar.jsl.utn.fra.ejercicios1;

public class Rectangulo {
    // Atrivutos
    private double ancho;
    private double alto;
    
    //Setter
    public void setAncho(double unAncho) {
        ancho = unAncho;
    }
    public void setAlto(double unAlto) {
        alto = unAlto;
    }
    
    //Getter
    public double getAncho() {
        return ancho;
    }
    public double getAlto() {
        return alto;
    }
    
    //Metodos
    public double calcularArea(double laAltura, double laAnchura) {
        double area = laAltura * laAnchura;
        return area;
    }
    public double calcularPerimetro(double laAltura, double laAnchura) {
        double perimetro = laAltura * 2 + laAnchura * 2;
        return perimetro;
    }
    public boolean esCuadrado() {
        return alto == ancho;
    }
}
