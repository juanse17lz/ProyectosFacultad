package sistemadegestiondeexpedicionesespaciales;

public class Carguero extends Nave implements Explorable {
    private int capacidadCarga;

    public Carguero(int capacidadCarga, String nombre, int capacidadDeTripulacion, int añoDeLanzamiento) {
        super(nombre, capacidadDeTripulacion, añoDeLanzamiento);
        this.capacidadCarga = capacidadCarga;
    }
    
    public int getCapacidadCarga() {
        return capacidadCarga;
    }
    
    @Override
    public void explorar() {
        System.out.println("El carguero " + getNombre() + " esta realizando la exploracion, su capacidad de carga es de " + capacidadCarga);
    }
}
