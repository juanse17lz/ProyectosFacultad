package ar.jsl.utn.fra.ejercicios1;

public class Producto {
    //Atributos
    private String nombre;
    private double precio;
    private int cantidadEnStock;
    
    //Setter
    public void setNombre(String unNombre) {
        nombre = unNombre;
    }
    public void setPrecio(double unPrecio) {
        precio = unPrecio;
    }
    public void setStock(int stockDisponible) {
        cantidadEnStock = stockDisponible;
    }
    
    //Getter
    public double getPrecio() {
        return precio;
    }
    public int getStock() {
        return cantidadEnStock;
    }
    
    //Metodos
    public void aplicarDescuento(int descuento) {
        precio = precio - precio * (descuento / 100);
    }
    public void realizarVenta() {
        if (cantidadEnStock > 0) {
            cantidadEnStock = cantidadEnStock - 1;
            System.out.println("Venta exitosa.");
        } else {
            System.out.println("No hay stock disponible.");
        }
    }
}
