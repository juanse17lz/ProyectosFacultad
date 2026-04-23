package constructor01;

public class Casa {
    private String direccion;
    private int habitaciones;
    private int pisos;
    private boolean tieneJardin;
    
    public Casa(String direccion, int habitaciones) {
        this.direccion = direccion;
        this.habitaciones = habitaciones;
        this.pisos = 0;
    }

    public String getDireccion() {
        return direccion;
    }

    public int getHabitaciones() {
        return habitaciones;
    }
    
}
