package ar.jsl.utn.fra.CuentaBancaria;

public class main {

    public static void main(String[] args) {
        CuentaBancaria s = new CuentaBancaria();
        s.setTitular("Juan Perez");
        System.out.println("Se creó una cuenta para: " + s.getTitular());
        System.out.println("Saldo actual: " + s.getSaldo());
        s.setSaldo(1000);
        System.out.println("Saldo actual: " + s.getSaldo());
        s.setRetiro(1500);
        s.setRetiro(500);
        System.out.println("Saldo actual: " + s.getSaldo());           
        
    }
    
}
