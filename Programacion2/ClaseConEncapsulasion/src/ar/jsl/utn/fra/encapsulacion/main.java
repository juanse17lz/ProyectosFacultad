package ar.jsl.utn.fra.encapsulacion;

public class main {

    public static void main(String[] args) {
        Persona p = new Persona();
        p.setNombre("Daniel");
        p.setEdad(54);
        System.out.println("Se llama " + p.getNombre() + " y tiene " + p.getEdad() + " años.");
    }
    
}
