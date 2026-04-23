package ar.jsl.utn.fra.ejercicios1;

public class Persona {
    //Atributos
    private String nombre;
    private int edad;
    private double altura;
    
    //Setter
    public void setNombre(String unNombre) {
        nombre = unNombre;
    }
    public void setEdad(int unaEdad) {
        edad = unaEdad;
    }
    public void setAltura(double unaAltura) {
        altura = unaAltura;
    }
    
    //Metodos
    public boolean esMayorDeEdad() {
        return edad >= 18;
    }
    public double IMC(int peso) {
        double indice = peso / (altura * altura);
        return indice;
    }
}
