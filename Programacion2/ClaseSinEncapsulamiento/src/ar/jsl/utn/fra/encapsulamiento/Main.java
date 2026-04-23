package ar.jsl.utn.fra.encapsulamiento;

public class Main {

    public static void main(String[] args) {  
        Persona p = new Persona();
        p.nombre = "Daniel";
        p.edad = -54; //Error logico
        System.out.println(p.nombre + " tiene " + p.edad + " años.");
    }
    
}
