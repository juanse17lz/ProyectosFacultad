package ar.jsl.utn.fra.ejercicios1;

public class Coche {
    //Atributos
    private String marca;
    private String modelo;
    private double kilometraje;
    private double combustibleRestante;
    
    //Setter
    public void setMarca(String unaMarca) {
        marca = unaMarca;
    }
    public void setModelo(String unModelo) {
        modelo = unModelo;
    }
    public void setKilometraje(double unKilometraje) {
        kilometraje = unKilometraje;
    }
    public void setCombustible(double unCombustible) {
        combustibleRestante = unCombustible;
    }
    
    //Getter
    public double getCombustible() {
        return combustibleRestante;
    }
    
    //Metodos
    public void recorridoPosible() {
        //Por cada litro de combustible se pueden recorrer 10 kilometros
        System.out.println("Se pueden recorrer " + (combustibleRestante * 10) + " kilometros." );
    }
    public void recargarCombustible(double recarga) {
        combustibleRestante = combustibleRestante + recarga;
    }
}
