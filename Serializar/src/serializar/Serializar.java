package serializar;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Serializar {
    public static void main(String[] args) {
        Persona tripulante = new Persona("Capitan Kirk", 35);
        
        try {
            FileOutputStream fos = new FileOutputStream("persona.dat");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            
            oos.writeObject(tripulante);
            
            oos.close();
            
        } catch (FileNotFoundException ex) {
            System.out.println("Error de archivo");
        } catch (IOException ex) {
            System.out.println("Error Input output.");
        }
        
        
    }
    
}
