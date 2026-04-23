package herencia01;

// Uso de protected: clases hija accedan a los atributos, pero no lo deja fuera del paquete. No asi cuando los atributos son privados.
// Constructor inicializa atributos comunes.
// avanzar() sera compartido por las subclases.

public class Vehiculo {
    //Atributos
    protected String color;
    protected int velocidad;
    protected int ruedas;
    
    //Constructor
    public Vehiculo(String color, int velocidad, int ruedas) {
        this.color = color;
        this.velocidad = velocidad;
        this.ruedas = ruedas;
    }
    
    //Metodo comun
    public void avanzar() {
        System.out.println("El vehiculo avanza a " + velocidad + " km/h.");
    }
    
    public void encender() {
        System.out.println("Encendiendo vehiculo...");
    }
}
