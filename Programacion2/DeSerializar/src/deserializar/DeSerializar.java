package deserializar;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class DeSerializar {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("C:\\Users\\juans\\Documents\\NetBeansProjects\\Serializar\\persona.dat");
            ObjectInputStream ois = new ObjectInputStream(fis);
        
            Persona tripulante = (Persona) ois.readObject();
            ois.close();
            
            System.out.println("Nombre: " + tripulante.getNombre());
            System.out.println("Edad: " + tripulante.getEdad());
            
        } catch (FileNotFoundException ex) {
            System.out.println("Error FileNotFound");
        } catch (IOException ex) {
            System.out.println("Error IOException");
        } catch (ClassNotFoundException ex) {
            System.out.println("Error ClassNotFound");
        }
    }
    
}
