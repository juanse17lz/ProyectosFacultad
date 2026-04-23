package ejercicio.viernes19.pkg9.semiparcial;
/*
-
- encendida: boolean
- volumen: int
- canal: int
- silencio boolean
-
+ encender(): void
+ apagar(): void
+ canalUp(): void
+ canalDown(): void
+ volumenUp(): void
+ volumenDown(): void
+ setCanal(nuevoCanal: int): void
+ setSilencio(): void
+ getCanal(): int
+ getVolumen(): int
+ estado(): String
+ isSilencio(): boolean
+ isEncendida(): boolean
*/
public class Tv {
    private boolean encendida = false;
    private int volumen = 10;
    private int canal = 1;
    private boolean silencio = false;
    
    public void encender() {
        encendida = true;
    }
    
    public void apagar() {
        encendida = false;
    }
    
    public void canalUp() {
        if (!encendida) return; //Chequeo si esta encendida
        if (canal >= 999) { //Se puede usar la funcion limitar
            canal = 1;
        } else {
            canal = canal + 1;
        }
    }
    
    public void canalDown() {
        if (!encendida) return; //Chequeo si esta encendida
        if (canal <= 1) {
            canal = 999;
        } else {
            canal = canal - 1;
        }
    }
    
    public void setCanal(int nuevoCanal) {
        if (!encendida) return; //Chequeo si esta encendida
        canal = limitar(nuevoCanal,1,999);
    }
    
    // Mantener valores de limites
    private int limitar(int valor, int min, int max) {
        if (valor < min) {
            return min;
        } else if (valor > max){
            return max;
        } else {
            return valor;
        }
    }
    
    public void volumenUp() {
        if (!encendida) return; //Chequeo si esta encendida
        silencio = false;
        volumen = limitar(volumen + 1, 0, 100);
    }
    
    public void volumenDown() {
        if (!encendida) return; //Chequeo si esta encendida
        silencio = false;
        volumen = limitar(volumen - 1, 0, 100);
    }
    
    public void setSilencio() { //Ver estado de volumen...
        if (!encendida) return; //Chequeo si esta encendida
        silencio = !silencio;
    }
/*    
+ getCanal(): int
+ getVolumen(): int
+ estado(): String
+ isSilencio(): boolean
+ isEncendida(): boolean
*/
    public boolean isEncendida() {
        return encendida;
    }
    
    public int getCanal() {
        return canal;
    }
    
    public int getVolumen() {
        return volumen;
    }
    
    public boolean isSilencio() {
        return silencio;
    }
    
    public String estado() {
        if (!encendida) return "Tv Apagada";
        String s = "Tv encendida | Canal: " + canal + " | Volumen: " + volumen;
        if (silencio) s = s + " (Silencio)";
        return s;
    }
}
