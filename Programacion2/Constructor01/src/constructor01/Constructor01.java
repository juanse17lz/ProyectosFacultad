package constructor01;

public class Constructor01 {
    public static void main(String[] args) {
        Casa c = new Casa("Calle 123",4);
        
        System.out.println(c.getDireccion());
        System.out.println(c.getHabitaciones());
    }
}
