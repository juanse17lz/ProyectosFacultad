package ar.jsl.utn.fra.ejercicios1;

public class Círculo {
    //Atributos
    private double radio;
    
    //Metodos
    //Setter
    public void setRadio(double unRadio) {
        radio = unRadio;
    }
    //Getter
    public double getRadio() {
        return radio;
    }
    public double calcularArea() {
        double area = 3.1416 * (radio * radio);
        return area;
    }
    public double calcularCircunferencia() {
        double circunferencia = 3.1416 * radio * 2;
        return circunferencia;
    }
    public void escalarCirculo(double porcentaje) {
        double escalamiento = radio * (porcentaje / 100);
            radio = radio + escalamiento;
    }
}
