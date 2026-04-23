package sistemadegestiondeexpedicionesespaciales;

public class NaveExploracion extends Nave implements Explorable {
    private TipoMision tipoMision;

    public NaveExploracion(String nombre, int capacidadDeTripulacion, int añoDeLanzamiento,TipoMision tipoMision) {
        super(nombre, capacidadDeTripulacion, añoDeLanzamiento);
        this.tipoMision = tipoMision;
    }
    
    public TipoMision getTipoMision() {
        return tipoMision;
    }
    
    @Override
    public void  explorar() {
        System.out.println("La nave de exploracion " + getNombre() + " esta iniciando su mision de " + tipoMision);
    }
}
