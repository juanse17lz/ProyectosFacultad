package ejercicio.viernes19.pkg9.semiparcial;

import java.util.Scanner;

public class EjercicioViernes199Semiparcial {
    public static void main(String[] args) {
        int canalIngresado;
        Tv tv = new Tv();
        ControlRemoto control = new ControlRemoto();
        control.emparejar(tv);
        
        Scanner sc = new Scanner(System.in);
        int opcion = -1;
        
        do {
            System.out.println("\n=========Control Remoto=========");
            System.out.println("1) Encender Tv");
            System.out.println("2) Apagar Tv");
            System.out.println("3) Canal +");
            System.out.println("4) Canal -");
            System.out.println("5) Setear Canal");
            System.out.println("6) Volumen +");
            System.out.println("7) Volumen -");
            System.out.println("8) Silencio On/Off");
            System.out.println("9) Ver Estado");
            System.out.println("0) Salir");
            System.out.println("Opcion: ");
            if (sc.hasNextInt()) {
                opcion = sc.nextInt();
            } else {
                sc.next();
                opcion = -1;
            }
            switch (opcion) {
                case 1:
                    control.encender();
                    break;
                case 2:
                    control.apagar();
                    break;
                case 3:
                    control.canalUp();
                    break;
                case 4:
                    control.canalDown();
                    break;
                case 5:
                    System.out.println("Ingrese canal (1..999): ");
                    if (sc.hasNextInt()) {
                        canalIngresado = sc.nextInt();
                    } else {
                        sc.nextInt();
                        canalIngresado = -1;
                    }
                    control.setCanal(canalIngresado);
                    break;
                case 6:
                    control.volumenUp();
                    break;
                case 7:
                    control.volumenDown();
                    break;
                case 8:
                    control.silenciar();
                    break;
                case 9:
                    System.out.println(control.estado());
                    break;
            }
        } while (opcion != 0);
        
        sc.close();
        System.out.println("Fin de la demo");
    }
    
}
