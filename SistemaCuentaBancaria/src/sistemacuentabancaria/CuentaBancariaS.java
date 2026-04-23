package sistemacuentabancaria;

public class CuentaBancariaS {
    protected int numCuenta;
    protected int saldo;
    protected String titular;

    public CuentaBancariaS(int numCuenta, int saldo, String titular) {
        this.numCuenta = numCuenta;
        this.saldo = saldo;
        this.titular = titular;
    }
    
    public void depositar(int monto) {
        if (monto > 0) {
            saldo = saldo + monto;
            System.out.println("Se deposito: " + monto + " - Nuevo saldo: " + saldo);
        } else {
            System.out.println("No se puede depositar un saldo negativo.");
        }
    }
    
    public void retirar(int monto, int limite) {
        if (saldo - monto >= limite) {
            saldo = saldo - monto;
            System.out.println("Se retiro: " + monto + " - Saldo restante: " + saldo);
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }
    
    public void mostrarDatos() {
        System.out.println("Datos de la Cuenta");
        System.out.println("Titular: " + titular);
        System.out.println("Numero de cuenta: " + numCuenta);
        System.out.println("Saldo: " + saldo);
    }
}
