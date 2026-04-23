package miprimerackase;

class Persona {
    // Atributos (estado del obejeto)
    String nombre;
    int edad;
    
    // Metodos (comportamientos de los objetos)
    public void saludar() {
        System.out.println("Hola, me llamo " + nombre + " y tengo" + edad + " años.");
    }
}

public class Main {
    public static void main(String[] args) {
        // Crear ojetos de la clase Persona
        Persona p1 = new Persona();
        Persona p2 = new Persona();
        
        // Asignar valores a los Objetos
        p1.nombre = "Ana";
        p1.edad = 25;
        
        p2.nombre = "Carlos";
        p2.edad = 30;
                
        // Llamar a los me
        p1.saludar();
        p2.saludar();
    }
}