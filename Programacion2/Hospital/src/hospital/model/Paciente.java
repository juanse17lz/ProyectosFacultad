package hospital.model;

public class Paciente {
    private String dni, nombre, apellido, obraSocial;

    public Paciente(String dni, String nombre, String apellido, String obraSocial) {
        this.dni = dni;
        this.nombre = nombre;
        this.apellido = apellido;
        this.obraSocial = obraSocial;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getObraSocial() {
        return obraSocial;
    }

    public void setObraSocial(String obraSocial) {
        this.obraSocial = obraSocial;
    }

    @Override
    public String toString() {
        return "Paciente{" + "dni=" + dni + ", nombre=" + nombre + ", apellido=" + apellido + ", obraSocial=" + obraSocial + '}';
    }
    
    
}
