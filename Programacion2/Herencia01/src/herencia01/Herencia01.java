package herencia01;

public class Herencia01 {
    public static void main(String[] args) {
        Auto alpine = new Auto(4,"Celeste", 120,4);
        Camion skania = new Camion(4, 50000, "Azul", 80, 18);
        
        alpine.mostrarInfo();
        alpine.avanzar();
        skania.mostrarInfo();
        skania.avanzar();
        
    }
    
}
