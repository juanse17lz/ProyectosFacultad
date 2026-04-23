package clase10;
import java.util.Scanner;

public class Clase10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Cuantos numeros desea ingresar?");
        int cantidad = scanner.nextInt();
        
        int[] numeros = new int[cantidad];
        
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("------------------------");
            System.out.println("Ingrese un numero " + (i + 1) + ": " );
            numeros[i] = scanner.nextInt();
        }
        
        System.out.println("======Resultados======");
        System.out.println("Los numeros ingresados son: ");
        for (int num : numeros) {
            System.out.println(num);
        }
    }
    
}
