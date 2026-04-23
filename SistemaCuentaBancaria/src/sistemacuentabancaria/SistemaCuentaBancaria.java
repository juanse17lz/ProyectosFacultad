package sistemacuentabancaria;

import java.util.Scanner;

public class SistemaCuentaBancaria {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int opcion;
        
        CajaDeAhorro nuevaA = null;
        CuentaCorriente nuevaC = null;
        
        do {
            
            System.out.println("\n====== Menu Cuenta Bancaria ======");
            System.out.println("1) Crear Caja de Ahorro");
            System.out.println("2) Crear Cuenta Corriente");
            System.out.println("3) Depositar");
            System.out.println("4) Retirar");
            System.out.println("5) Mostrar informacion de la cuenta");
            System.out.println("0) Salir");
            System.out.println("Elige una opcion");

            opcion = sc.nextInt();
            sc.nextLine();
            
            switch(opcion) {
                case 1 -> {
                    System.out.println("Ingrese el titular de la cuenta: ");
                    String nombre = sc.nextLine();
                    nuevaA = new CajaDeAhorro(0,101,0,nombre);
                    nuevaA.mostrarDatos();
                }
                case 2 -> {
                    System.out.println("Ingrese el titular de la cuenta: ");
                    String nombre = sc.nextLine();
                    nuevaC = new CuentaCorriente(-50000,201,0,nombre);
                    nuevaC.mostrarDatos();
                }
                case 3 -> {
                    System.out.println("Desea depositar en: 1 - Caja de Ahorro / 2 - Cuenta corriente");
                    int opcionDeposito = sc.nextInt();
                    sc.nextLine();
                    switch(opcionDeposito) {
                        case 1 -> {
                            System.out.println("Ingrese el monto a depositar en la Caja de Ahorro: ");
                            int montoA = sc.nextInt();
                            nuevaA.depositar(montoA);
                        }
                        case 2 -> {
                            System.out.println("Ingrese el monto a depositar en la Cuenta Corriente: ");
                            int montoC = sc.nextInt();
                            nuevaC.depositar(montoC);
                        }
                    }
                }
                case 4 -> {
                    System.out.println("Desea retirar de: 1 - Caja de Ahorro / 2 - Cuenta corriente");
                    int opcionRetiro = sc.nextInt();
                    sc.nextLine();
                    switch(opcionRetiro) {
                        case 1 -> {
                            System.out.println("Ingrese el monto a retirar de la Caja de Ahorro: ");
                            int montoA = sc.nextInt();
                            nuevaA.RetirarCajaDeAhorro(montoA);
                        }
                        case 2 -> {
                            System.out.println("Ingrese el monto a retirar de la Cuenta Corriente: ");
                            int montoC = sc.nextInt();
                            nuevaC.RetirarCuentaCorriente(montoC);
                        }
                    }
                }
                case 5 -> {
                    System.out.println("Desea consultar la informacion de: 1 - Caja de Ahorro / 2 - Cuenta corriente");
                    int opcionConsulta = sc.nextInt();
                    sc.nextLine();
                    switch(opcionConsulta) {
                        case 1 -> nuevaA.mostrarDatos();
                        case 2 -> nuevaC.mostrarDatos();
                    }
                }
            }
        } while(opcion != 0);
    }
}
