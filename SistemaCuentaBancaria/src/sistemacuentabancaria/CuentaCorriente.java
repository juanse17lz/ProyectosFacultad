package sistemacuentabancaria;

public class CuentaCorriente extends CuentaBancariaS {
    private int limiteDescubierto;

    public CuentaCorriente(int limiteDescubierto, int numCuenta, int saldo, String titular) {
        super(numCuenta, saldo, titular);
        this.limiteDescubierto = limiteDescubierto;
    }
    
    public void RetirarCuentaCorriente(int monto) {
        this.retirar(monto, limiteDescubierto);
    }
}
