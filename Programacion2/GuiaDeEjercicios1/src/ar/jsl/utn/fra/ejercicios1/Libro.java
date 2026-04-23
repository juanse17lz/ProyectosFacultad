package ar.jsl.utn.fra.ejercicios1;

public class Libro {
    //Atributos
    private String titulo;
    private String autor;
    private int numeroDePaginas;
    private int paginaActual;
    
    //Setter
    public void setNumeroDePaginas(int cantidadDePaginas) {
        numeroDePaginas = cantidadDePaginas;
    }
    public void setPaginaActual(int pagActual) {
        paginaActual = pagActual;
    }
    
    //Metodos
    public boolean libroTerminado() {
        return paginaActual == numeroDePaginas;
    }
    public void avanzarPagina() {
        paginaActual = paginaActual + 1;
        System.out.println("Avanzando de pagina.");
        if (libroTerminado()==true) {
            System.out.println("El libro ha sido termindao.");
        } 
    }
    public void retocederPagina() {
        paginaActual = paginaActual - 1;
    }
}
