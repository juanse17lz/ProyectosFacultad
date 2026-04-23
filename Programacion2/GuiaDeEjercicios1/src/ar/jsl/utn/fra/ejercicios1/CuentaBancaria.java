package ar.jsl.utn.fra.ejercicios1;

public class CuentaBancaria {
    //Atrivutos Privados
    private double saldo;
    private String titular;
    private int numeroDeCuenta;
    
    //Getter
    public double getSaldo() {
        return saldo;
    }
    public String getTitular() {
        return titular;
    }
    
    //Setter
    public void setSaldo(double unSaldo) {
        if (unSaldo > 0) {
            saldo = unSaldo;
            System.out.println("Depositando: " + unSaldo);
        } else {
            System.out.println("El saldo debe ser positivo.");
        }
    }
    public void setTitular(String unTitular) {
        titular = unTitular;
    }
    public void setRetiro(double unRetiro) {
        System.out.println("Intentando retirar: " + unRetiro);
        if (saldo - unRetiro > 0) {
            saldo = saldo - unRetiro;
            System.out.println("Retirando: " + unRetiro);
        } else {
            System.out.println("Fondos insuficientes.");
        }
    }
}
