package ar.jsl.utn.fra.BancoBasico;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        CuentaBancaria cuenta = new CuentaBancaria();
        
        int opcion;
        do {
            
            System.out.println("\n====== Menu Cuenta Bancaria ======");
            System.out.println("1) Definir el Titular");
            System.out.println("2) Depositar");
            System.out.println("3) Retirar");
            System.out.println("4) Consultar el saldo");
            System.out.println("5) Consultar el Titular");
            System.out.println("0) Salir");
            System.out.println("Elige una opcion");
            
            opcion = sc.nextInt(); // int(input(""))
            sc.nextLine(); // Limpiar el buffer
            
            switch (opcion) {
                case 1 -> {
                    System.out.println("Ingrese el nombre del Titular: ");
                    String nombre = sc.nextLine();
                    cuenta.setTitular(nombre);
                }
                case 2 -> {
                    System.out.println("Ingrese el monto a depositar: ");
                    double monto = sc.nextDouble();
                    cuenta.setSaldo(monto);
                }
                case 3 -> {
                    System.out.println("Ingrese el monto a retirar: ");
                    double retiro = sc.nextDouble();
                    cuenta.setRetiro(retiro);
                }
                case 4 ->System.out.println("Saldo actual: " + cuenta.getSaldo());
                
                case 5 ->System.out.println("El titular es: " + cuenta.getTitular());
                
                case 0 ->System.out.println("Gracias por usar el sistema.");
            }
        } while(opcion != 0);
    }
    
}
