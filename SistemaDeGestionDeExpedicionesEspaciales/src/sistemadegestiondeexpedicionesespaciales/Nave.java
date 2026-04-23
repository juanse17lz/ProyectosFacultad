package sistemadegestiondeexpedicionesespaciales;

import java.util.Objects;

public class Nave {
    private String nombre;
    private int capacidadDeTripulacion;
    private int añoDeLanzamiento;

    public Nave(String nombre, int capacidadDeTripulacion, int añoDeLanzamiento) {
        this.nombre = nombre;
        this.capacidadDeTripulacion = capacidadDeTripulacion;
        this.añoDeLanzamiento = añoDeLanzamiento;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public int getCapacidad() {
        return capacidadDeTripulacion;
    }
    
    public int getAñoLanzamiento() {
        return añoDeLanzamiento;
    }
    

}    

