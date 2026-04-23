package ejercicio.viernes19.pkg9.semiparcial;

public class ControlRemoto {
    private Tv tv; //Colaboracion: control conoce la tv
    
    public void emparejar(Tv tv) {
        this.tv = tv;
    }
    
    public boolean hayTv() {
        return tv != null;
    }
    
    public void encender() {
        if (hayTv())
            tv.encender();
    }
    
    public void apagar() {
        if (hayTv())
            tv.apagar();
    }
    
    public void canalUp() {
        if (hayTv())
            tv.canalUp();
    }
    
    public void canalDown() {
        if (hayTv())
            tv.canalDown();
    }
    
    public void setCanal(int c) {
        if (hayTv())
            tv.setCanal(c);
    }
    
    public void volumenUp() {
        if (hayTv())
            tv.volumenUp();
    }
    
    public void volumenDown() {
        if (hayTv())
            tv.volumenDown();
    }
    
    public void silenciar() {
        if (hayTv())
            tv.setSilencio();
    }
    
    public String estado() {
        if (!hayTv()) return "Sin tv emparejada";
        return tv.estado();
    }
}
