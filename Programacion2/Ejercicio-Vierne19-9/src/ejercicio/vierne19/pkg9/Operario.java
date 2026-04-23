package ejercicio.vierne19.pkg9;

public class Operario extends Empleado {
    public Operario(String nombre, int horasTrabajadas) {
        super(nombre, horasTrabajadas);
    }
    
    @Override
    public void calcularSueldo() {
        double sueldo = horasTrabajadas * 1500;
        System.out.println("El empleado " + nombre + " tiene el puesto de Operario y su sueldo es de $" + sueldo);
    }
}
