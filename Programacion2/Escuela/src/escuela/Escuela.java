package escuela;

public class Escuela {

    public static void main(String[] args) {
        Estudiante e = new Estudiante("Juan",24);
        Profesor p = new Profesor("Daniel",50);
        
        e.presentarse();
        p.presentarse();
    }
    
}
