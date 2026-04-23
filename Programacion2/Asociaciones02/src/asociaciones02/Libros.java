package asociaciones02;

public class Libros {
    private String titulo;
    private String autor;
    private int siguienteID = 0;
    private String añoDePublicacion;
    
    public Libros(String titulo, String autor, int siguienteID, String añoDePublicacion) {
        this.titulo = titulo;
        this.autor = autor;
        this.siguienteID = siguienteID;
        this.añoDePublicacion = añoDePublicacion;
    }
    
    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getSiguienteID() {
        return siguienteID;
    }

    public String getAñoDePublicacion() {
        return añoDePublicacion;
    }

    public void setTitulo(String unTitulo) {
        this.titulo = unTitulo;
    }    
    

}
