package ejercicio.vierne19.pkg9;

public class Empleado {
    protected String nombre;
    protected int horasTrabajadas;

    public Empleado(String nombre, int horasTrabajadas) {
        this.nombre = nombre;
        this.horasTrabajadas = horasTrabajadas;
    }
          
    public void calcularSueldo() {
        double sueldo = horasTrabajadas * 1000;
        System.out.println("El sueldo generico de un empleado es de $" + sueldo);
    }
    
}
