package herencia01;

public class Camion extends Vehiculo {
    private int puertas;
    private int cargaMaxima;

    public Camion(int puertas, int cargaMaxima, String color, int velocidad, int ruedas) {
        super(color, velocidad, ruedas);
        this.puertas = puertas;
        this.cargaMaxima = cargaMaxima;
    }
    
    public void mostrarInfo() {
        System.out.println("Camion de color " + this.color + 
                ", velocidad: " + this.velocidad + " km/h " +
                ", puertas: " + this.puertas + 
                ", ruedas: " + this.ruedas +
                ", carga maxima: " + this.cargaMaxima);
    }
    
}
