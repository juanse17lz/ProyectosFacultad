package sistemadegestiondeexpedicionesespaciales;

import java.util.ArrayList;
import java.util.List;

public class GestorDeNaves {
    private List<Nave> naves;
   
    public GestorDeNaves() {
        naves = new ArrayList<>();
    }
    
    public void agregarNave(Nave nave) throws NaveDuplicadaExcepcion {
        for (Nave naveExistente : naves){
            if (naveExistente.getNombre().equals(nave.getNombre()) && naveExistente.getAñoLanzamiento() == nave.getAñoLanzamiento()) {
                throw new NaveDuplicadaExcepcion("La nave " + nave.getNombre() + " con año de lanzamiento " + nave.getAñoLanzamiento() + " ya existe.");
            }
        }
        naves.add(nave);
        System.out.println("Nave " + nave.getNombre() + " fue agregada exitosamente.");
    }
    
    public void eliminarNave(String nombre, int año) {
        boolean encontrada = false;
        for (int i = 0; i < naves.size(); i++) {
            Nave nave = naves.get(i);
            if (nave.getNombre().equals(nombre) && nave.getAñoLanzamiento() == año) {
                naves.remove(i);
                System.out.println("Nave eliminada exitosamente.");
                encontrada = true;
                break;
            }
        }
        
        if (!encontrada) {
            System.out.println("La nave " + nombre + " con año de lanzamiento " + año + " no se encuentra registrada.");
        }
    }
    
    public void iniciarExploracion(Nave nave) {
        System.out.println("===== Iniciar Exploracion =====");
                
        if (nave instanceof Explorable) {
            Explorable naveExplorable = (Explorable) nave;
            naveExplorable.explorar();
            naves.remove(nave);
            System.out.println("\n----- LA NAVE " + nave.getNombre() + " ESTA REALIZANDO SU MISION -----");
            System.out.println("\nMision Finalizada.");
            System.out.println("La nave " + nave.getNombre() + " fue eliminada de los registros tras la finalizacion de su mision.");
        } else {
            System.out.println("La nave " + nave.getNombre() + " no es una nave de exploracion.");
        }        
    }
    
    public Nave buscarNave(String nombre, int año) {
        for (Nave nave : naves) {
            if (nave.getNombre().equals(nombre) && nave.getAñoLanzamiento() == año) {
                return nave;
            }
        }
        System.out.println("No hay registro de la nave solicitada.");
        return null;
    } 
    
    public void mostrarNaves() {
        System.out.println("===== Naves =====");
        if (naves.isEmpty()) {
            System.out.println("No hay naves ingresadas.");
        } else {
            for (Nave nave : naves) {
                if (nave instanceof Explorable) {
                    if (nave instanceof NaveExploracion) {
                        System.out.println("- Nombre: " + nave.getNombre() + " - Año de Lanzamiento: " + nave.getAñoLanzamiento() + " - Tripulacion: " + nave.getCapacidad() + " - Mision: " + ((NaveExploracion) nave).getTipoMision());
                    } else {
                        if (nave instanceof Carguero) {
                            System.out.println("- Nombre: " + nave.getNombre() + " - Año de Lanzamiento: " + nave.getAñoLanzamiento() + " - Tripulacion: " + nave.getCapacidad() + " - Capacidad de Carga: " +  ((Carguero) nave).getCapacidadCarga());                    
                        }
                    }
                } else {
                    if (nave instanceof CruceroEstelar) {    
                        System.out.println("- Nombre: " + nave.getNombre() + " - Año de Lanzamiento: " + nave.getAñoLanzamiento() + " - Tripulacion: " + nave.getCapacidad() +  " - Capacidad de Pasajeros: " + ((CruceroEstelar) nave).getPasajeros());
                    }
                }
            }
        }
    }
    
}
