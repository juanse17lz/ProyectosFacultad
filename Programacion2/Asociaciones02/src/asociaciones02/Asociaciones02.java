package asociaciones02;

public class Asociaciones02 {
    public static void main(String[] args) {
        Biblioteca b1 = new Biblioteca();
        b1.setNombre("Biologia");
        
        Libros libro1 = new Libros("Anatomia","Francisico",1,"1898");
        Libros libro2 = new Libros("Enfermedades","Carlos",2,"1934");
        Libros libro3 = new Libros("Sistemas Nerviosos","Agusto",3,"1957");

        b1.agregarLibro(libro1);
        b1.agregarLibro(libro2);
        b1.agregarLibro(libro3);
        
        b1.mostrarLibros();
    }    
}
