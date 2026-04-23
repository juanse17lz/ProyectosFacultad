package sistemacuentabancaria;

public class CajaDeAhorro extends CuentaBancariaS {
    private int limite;

    public CajaDeAhorro(int limite, int numCuenta, int saldo, String titular) {
        super(numCuenta, saldo, titular);
        this.limite = limite;
    }
    
    public void RetirarCajaDeAhorro(int monto) {
        this.retirar(monto, limite);
    }
}
