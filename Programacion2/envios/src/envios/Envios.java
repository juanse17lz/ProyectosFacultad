package envios;

public class Envios {
    public static void main(String[] args) {
        // Uso polimórfico
        CotizadorEnvios normal = new CotizadorEnvios();
        CotizadorExpress express = new CotizadorExpress();
        CotizadorEconomico economico = new CotizadorEconomico();

        // Sobrecarga en CotizadorEnvios
        double c1 = normal.cotizar(2.0);                  // solo peso
        double c2 = normal.cotizar(3.5, "NACIONAL");      // peso + destino
        double c3 = normal.cotizar(2.0, 40, 30, 50);      // peso volumétrico

        // Sobreescritura en subclases
        double c4 = express.cotizar(2.0);                 // Express redefine cotizar
        double c5 = economico.cotizar(2.0);               // Económico redefine cotizar

        System.out.println("Normal (solo peso): $" + c1);
        System.out.println("Normal (peso + destino): $" + c2);
        System.out.println("Normal (volumétrico): $" + c3);
        System.out.println("Express (sobreescritura): $" + c4);
        System.out.println("Económico (sobreescritura): $" + c5);
    }
    
}
