package ar.jsl.utn.fra.asosciaciones;

import java.util.ArrayList;

public class Profesor {
    
    private String nombre;
    private ArrayList<Curso> cursos = new ArrayList<>(); // Asociacion 1-N
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String string) {
        this.nombre = string;
    }
    
    //Agregar un curso a la lista
    public void argregarCurso(Curso curso) {
        cursos.add(curso);
    }
    
    //Mostrar todos los cursos que dicta un profesor
    public void mostrarCursos() {
        System.out.println("Profesor: " + nombre);
        System.out.println("Crusos que dicta: ");
        //foreach
        for (Curso c : cursos) {
            System.out.println("- " + c.getNombre());
        }
    }
}
