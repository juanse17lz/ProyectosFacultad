package excepciones;

import java.util.Scanner;

public class Excepciones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingrese su edad: ");
        int edad = Integer.parseInt(sc.nextLine());//Punto debil: puede ingresarse otra cosas ademas de enteros
        
        int aniosRestantes = 65 - edad;
        if(aniosRestantes > 0) {
            System.out.println("Faltan " + aniosRestantes + " para jubilarte.");
        } else {
            System.out.println("Ya tiene la edad para jubilarse.");
        }
    }
    
}
