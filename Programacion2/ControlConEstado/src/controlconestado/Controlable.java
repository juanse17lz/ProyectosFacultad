package controlconestado;
/*
Interfaz que define las acciones basicas de un dispositivo controlable.
*/
public interface Controlable {
    void encender();
    void apagar();
    void subirVolumen();
    void bajarVolumen();
    void canalUp();
    void canalDown();
    void setCanal(int nuevoCanal);
    boolean estaEncendido();
    String infoEstado();
}
