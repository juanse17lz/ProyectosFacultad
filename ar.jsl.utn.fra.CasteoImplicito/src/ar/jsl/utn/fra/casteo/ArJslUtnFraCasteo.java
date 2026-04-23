/*
Java convierte el int a un double: lo hace automaticamente porqie no hay riesgo de datos.

package ar.jsl.utn.fra.casteo;

public class ArJslUtnFraCasteoImplicito {
    public static void main(String[] args) {
        int num = 100;
        double valor = num; // Casteo implicito int --> double
        
        System.out.println("Entero: " + num);
        System.out.println("Convertido a double: " + valor);
    }
}



Aqui necescitamos un (int) porque pasar de double a int se pierden los decimales.

package ar.jsl.utn.fra.casteo;

public class ArJslUtnFraCasteo {
    public static void main(String[] args) {
        double valor = 9.78;
        int num = (int) valor; // Casteo explicito double --> int
        
        System.out.println("Entero: " + num);
        System.out.println("Double: " + valor);
    }
    
}
*/
package ar.jsl.utn.fra.casteo;

public class ArJslUtnFraCasteo {
    public static void main(String[] args) {
        // Upcasting (implicito) -> instancia Perro() es un Animal().
        Animal a = new Perro(); 
        Animal b = new Gato();
        a.hacerSonido();// Llama al metodo sobreescrito en Perro() 
        sonido(a);
        b.hacerSonido();// Llama al metodo sobreescrito en Gato() 
        // Error: a.moverCola(); // utiliza exclusivamente en el tipo de la referencia
        a.comer(); // Comer de la clase animal
        b.comer(); // Comer de la clase animal
        // Downcasting (explicito)
        Perro p = (Perro) a;
        p.moverCola(); // Ahora si podemos acceder al metodo especifico de Perro.
        
        //Perro p2 = (Perro) b; // Error de tiempo de ejecucion
        //p2.hacerSonido();
        if (b instanceof Gato) {
            Gato p2 = (Gato) b;
            p2.hacerSonido();
            sonido(p2);
        } else {
            Perro p2  = (Perro) b;
            p2.hacerSonido();
        }
       
    }
    
    private static void sonido(Animal animalLocal) {
        animalLocal.hacerSonido();
    }
}

class Animal {
    public void hacerSonido() {
        System.out.println("Sonido generico de animal.");
    }
    
    public void comer() {
        System.out.println("Comer de animal.");
    }
}

class Perro extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("Guau Guau");
    }
    
    public void moverCola() {
        System.out.println("El perro mueve la cola.");
    } 
}

class Gato extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("Miau Miau");
    }
    
    public void saltar() {
        System.out.println("El gato salta.");
    }
}