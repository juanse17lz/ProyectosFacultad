package ar.jsl.utn.fra.ejercicios1;

public class Reloj {
    //Atributos
    private int hora;
    private int minutos;
    private int segundos;
    
    //Setter
    public void setHora(int unaHora) {
        if (unaHora >= 0 && unaHora < 24) {
            hora = unaHora;
        } else {
            System.out.println("La hora no se puede settear.");
        }
    }
    public void setMinutos(int unMinuto) {
        if (unMinuto >= 0 && unMinuto < 60) {
            minutos = unMinuto;
        } else {
            System.out.println("Los minutos no se pueden settear.");
        }
    }
    public void setSegundos(int unSegundo) {
        if(unSegundo >= 0 && unSegundo < 60) {
            segundos = unSegundo;
        } else {
            System.out.println("Los segundos no se pueden settear.");
        }
    }
    
    //Getter
    public int getHora() {
        return hora;
    }
    public int getMinutos() {
        return minutos;
    }
    public int getSegundos() {
        return segundos;
    }
    
    //Metodos
    public void avanzarTiempo() {
        segundos = segundos + 1;
        if (segundos == 60) {
            segundos = 0;
            minutos = minutos +1;
            if (minutos == 60) {
                minutos = 0;
                hora = hora + 1;
                if (hora == 24) {
                    hora = 0;
                }
            }
        }
    }
}
