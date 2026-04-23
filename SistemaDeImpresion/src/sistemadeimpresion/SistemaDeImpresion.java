package sistemadeimpresion;

public class SistemaDeImpresion {

    public static void main(String[] args) {
        Impresora imp = new Impresora();
        
        imp.imprimir("Hola Mundo");
        imp.imprimir(123);
        imp.imprimir("Saludos", 3);
    }
    
}
