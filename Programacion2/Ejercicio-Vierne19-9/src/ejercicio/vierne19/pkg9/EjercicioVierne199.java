package ejercicio.vierne19.pkg9;

public class EjercicioVierne199 {
    public static void main(String[] args) {
        Empleado a = new Gerente("Juan Lopez", 10);
        Empleado b = new Operario("Joaquin Lopez",15);
        
        a.calcularSueldo();
        b.calcularSueldo();
    }    
}
