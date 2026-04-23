package ar.jsl.utn.fra.asosciaciones;

public class main {
    public static void main(String[] args) {
        Profesor profesor = new Profesor();
        profesor.setNombre("Cristian");
        
        Curso curso1 = new Curso();
        Curso curso2 = new Curso();
        Curso curso3 = new Curso();
        
        curso1.setNombre("Programacion 2");
        curso2.setNombre("Base de Datos");
        curso3.setNombre("Java Avanzado");
        
        profesor.argregarCurso(curso1);
        profesor.argregarCurso(curso2);
        profesor.argregarCurso(curso3);
        
        profesor.mostrarCursos();
    }    
}
