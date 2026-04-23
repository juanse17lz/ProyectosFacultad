package ar.jsl.utn.fra.encapsulacion;

public class Persona {
    //Atributos Privados
    private String nombre;
    private int edad;
    
    //Getter 
    public String getNombre() {
        return nombre;
    }
    public int getEdad() {
        return edad;
    }
    
    //Setter
    public void setNombre(String unNombre) {
        nombre = unNombre;
    }
    public void setEdad(int unaEdad) {
        if (unaEdad > 0) {
            edad = unaEdad;
        } else {
            System.out.println("La edad debe ser positiva.");
        }        
    }
}
