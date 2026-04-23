package controlconestado;

public class Tv implements Controlable{
    private boolean encendido;
    private int volumen;
    private int canal;
    private String fuente;

    public Tv() {
        this.encendido = false;
        this.volumen = 10;
        this.canal = 1;
        this.fuente = "HDMI1";
    }
    
    

    @Override
    public void encender() {
        encendido = true;
        System.out.println("[TV] Encendido");
    }

    @Override
    public void apagar() {
        encendido = false;
        System.out.println("[TV] Apagada");
    }

    @Override
    public void subirVolumen() {
        if (encendido && volumen < 100) volumen++;
    }

    @Override
    public void bajarVolumen() {
        if (encendido && volumen > 1) volumen--;
    }

    @Override
    public void canalUp() {
        if (!encendido) return; //Chequeo si esta encendida
        if (canal >= 999) { //Se puede usar la funcion limitar
            canal = 1;
        } else {
            canal = canal + 1;
        }
    }

    @Override
    public void canalDown() {
        if (!encendido) return; //Chequeo si esta encendida
        if (canal <= 1) {
            canal = 999;
        } else {
            canal = canal - 1;
        }
    }

    @Override
    public void setCanal(int nuevoCanal) {
        if (!encendido) return; //Chequeo si esta encendida
        canal = limitar(nuevoCanal,1,999);
    }

    @Override
    public boolean estaEncendido() {
        return encendido;
    }

    @Override
    public String infoEstado() {
        if (!encendido) return "Tv Apagada";
        String s = "Tv encendida: " + encendido + " | Canal: " + canal + " | Volumen: " + volumen + " | Fuente: " + fuente;
        return s;
    }
    
    private int limitar(int valor, int min, int max) {
        if (valor < min) {
            return min;
        } else if (valor > max){
            return max;
        } else {
            return valor;
        }
    }
    
    
}
