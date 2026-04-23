package sistemadeimpresion;

public class Impresora {
    public void imprimir(String texto) {
        System.out.println("Imprimiendo texto: " + texto);
    }
    
    public void imprimir(int numero) {
        System.out.println("Imprimiendo: " + numero);
    }
    
    public void imprimir(String texto, int veces) {
        for (int i = 0; i < veces; i ++) {
            System.out.println("Copia " + (i+1) + ": " + texto);
        }
    }
}
