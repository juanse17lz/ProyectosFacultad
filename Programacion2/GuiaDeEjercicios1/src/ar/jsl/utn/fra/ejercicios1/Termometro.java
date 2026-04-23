package ar.jsl.utn.fra.ejercicios1;

public class Termometro {
    //Atributos
    private double temperatura;
    private boolean medicion;
    
    //Setter
    public void setTemperatura(double unaTemperatura) {
        temperatura = unaTemperatura;
    }
    public void setMedicion(boolean unaMedicion) {
        medicion = unaMedicion;
    }
    //Getter
    public double getTemperatura() {
        return temperatura;
    }
    
    //Metodos
    public void cambiarMedicion() {
        if (medicion == true) {
            temperatura = (temperatura * (9/5)) + 32;
            medicion = false;
        } else {
            temperatura = (temperatura - 32) * (5/9);
            medicion = true;
        }
    }
    public void modificarTemperatura(double aumentoDescensoTemperatura) {
        if (medicion == true) {
            temperatura = temperatura + (1 * aumentoDescensoTemperatura);
        } else {
            temperatura = temperatura + (1.8 * aumentoDescensoTemperatura);
        }
    }
}
