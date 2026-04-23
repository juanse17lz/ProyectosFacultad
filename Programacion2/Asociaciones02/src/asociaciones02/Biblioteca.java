package asociaciones02;

import java.util.ArrayList;

public class Biblioteca { 
    private String nombre;
    private ArrayList <Libros> libro = new ArrayList<>();
    private int nextID = 0;

    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String unNombre) {
        this.nombre = unNombre;
    }
    
    public void agregarLibro(Libros unLibro) {
        libro.add(unLibro);
    }
    
    public void mostrarLibros() {
        System.out.println("Biblioteca: " + nombre);
        System.out.println("Libros que contiene: ");
        for (Libros c : libro) {
            System.out.println("Titulo: " + c.getTitulo() + " - Autor: " + c.getAutor() + " - Año de Publicacion: " + c.getAñoDePublicacion());
        }
    }
}
