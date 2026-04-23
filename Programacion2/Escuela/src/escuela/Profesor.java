package escuela;

public class Profesor extends Persona {

    public Profesor(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void presentarse() {
        System.out.println("El profesor " + nombre + " tiene " + edad + " años.");
    }
}
