package herencia01;

public class Auto extends Vehiculo {
    private int puertas;

    public Auto(int puertas, String color, int velocidad, int ruedas) {
        super(color, velocidad, ruedas); //Primer linea del contructor.
        this.puertas = puertas;
    }
    
    public void mostrarInfo() {
        System.out.println("Auto de color " + this.color + 
                ", velocidad: " + this.velocidad + " km/h " +
                ", puertas: " + this.puertas + 
                ", ruedas: " + this.ruedas);
    }
    
    @Override
    public void encender() {
        System.out.println("Encendiendo auto.");
    }
}
