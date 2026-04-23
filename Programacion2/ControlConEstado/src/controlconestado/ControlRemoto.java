package controlconestado;

public class ControlRemoto {
        private Tv tv;
        private Decodificador deco;
        private Controlable activo = tv;
    
    public void emparejarTv(Tv tv) {
        this.tv = tv;
    }    
    
    public void emparejarDeco(Decodificador deco) {
        this.deco = deco;
    }
    
    public void cambiarControl() {
        if (activo == tv) {
            activo = deco;
            System.out.println("Controlando Deco");
        } else {
            activo = tv;
            System.out.println("Controlando la Tv");
        }
    }
    
    private String nombreActivo() {
        if (activo == tv)
            return "TV";
        else
            return "DECO";
    }
    
    public void botonEncendido() {
        System.out.println("[Controlando: " + nombreActivo() + "]");
        if (activo.estaEncendido()) {
            activo.apagar();
        } else {
            activo.encender();
        }
    }
    
    public void emparejar(Tv tv) {
        this.tv = tv;
    }
    
    public boolean hayTv() {
        return tv != null;
    }
    
    public void encender() {
        if (activo == tv)
            tv.encender();
        else
            deco.encender();
    }
    
    public void apagar() {
        if (activo == tv)
            tv.apagar();
        else
            deco.apagar();
    }
    
    public void canalUp() {
        if (activo == tv)
            tv.canalUp();
        else
            deco.canalUp();
    }
    
    public void canalDown() {
        if (activo == tv)
            tv.canalDown();
        else
            deco.canalDown();
    }
    
    public void setCanal(int c) {
        if (activo == tv)
            tv.setCanal(c);
        else
            deco.setCanal(c);
    }
    
    public void volumenUp() {
        if (activo == tv)
            tv.subirVolumen();
        else
            deco.subirVolumen();
    }
    
    public void volumenDown() {
        if (activo == tv)
            tv.bajarVolumen();
        else
            deco.bajarVolumen();
    }
    
    public String estado() {
        if (activo == tv) {
            return tv.infoEstado();
        } else {
            return deco.infoEstado();}
    }
    
    public void estaEncendido() {
        if (activo == tv)
            System.out.println(tv.estaEncendido());
        else
            System.out.println(deco.estaEncendido());
    }
}
