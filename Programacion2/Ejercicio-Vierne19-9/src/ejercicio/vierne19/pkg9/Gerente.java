package ejercicio.vierne19.pkg9;

public class Gerente extends Empleado {
    public Gerente(String nombre, int horasTrabajadas) {
        super(nombre, horasTrabajadas);
    }
    
    @Override
    public void calcularSueldo() {
        double sueldo = horasTrabajadas * 2500;
        System.out.println("El empleado " + nombre + " tiene el puesto de Gerente y su sueldo es de $" + sueldo);
    }
}
