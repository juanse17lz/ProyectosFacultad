package sistemadegestiondeexpedicionesespaciales;

public class CruceroEstelar extends Nave {
    private int cantidadPasajeros;

    public CruceroEstelar(int cantidadPasajeros, String nombre, int capacidadDeTripulacion, int añoDeLanzamiento) {
        super(nombre, capacidadDeTripulacion, añoDeLanzamiento);
        this.cantidadPasajeros = cantidadPasajeros;
    }
    
    public int getPasajeros() {
        return cantidadPasajeros;
    }    
}
