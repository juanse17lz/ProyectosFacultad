package escuela;

public class Estudiante extends Persona {

    public Estudiante(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void presentarse() {
        System.out.println("El estudiante " + nombre + " tiene " + edad + " años.");
    }
}
