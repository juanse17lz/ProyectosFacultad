package ar.jsl.utn.fra.ejercicios1;

public class main {
    public static void main(String[] args) {
        //Rectangulo
        Rectangulo r = new Rectangulo();
        r.setAlto(10);
        r.setAncho(5);
        System.out.println(r.calcularArea(r.getAlto(),r.getAncho()));
        System.out.println(r.calcularPerimetro(r.getAlto(),r.getAncho()));
        System.out.println(r.esCuadrado());
        System.out.println("-----------------------------------------------------");
        
        //Circulo
        Círculo c = new Círculo();
        c.setRadio(5);
        System.out.println(c.calcularArea());
        System.out.println(c.calcularCircunferencia());
        c.escalarCirculo(100);
        System.out.println(c.getRadio());
        System.out.println("-----------------------------------------------------");
        
        //Persona
        Persona p = new Persona();
        p.setNombre("Juan");
        p.setEdad(18);
        p.setAltura(1.75);
        System.out.println(p.esMayorDeEdad());
        System.out.println(p.IMC(70));
        System.out.println("-----------------------------------------------------");
        
        //Coche
        Coche ch = new Coche();
        ch.setCombustible(25);
        ch.recorridoPosible();
        ch.recargarCombustible(15);
        System.out.println(ch.getCombustible());
        System.out.println("-----------------------------------------------------");
        
        //Libro
        Libro l = new Libro();
        l.setNumeroDePaginas(3);
        l.setPaginaActual(1);
        l.avanzarPagina();
        l.avanzarPagina();
        System.out.println("-----------------------------------------------------");
        
        //Termometro
        Termometro t = new Termometro();
        t.setTemperatura(25);
        t.setMedicion(true);
        System.out.println(t.getTemperatura());
        t.cambiarMedicion();
        System.out.println(t.getTemperatura());
        t.cambiarMedicion();
        t.modificarTemperatura(5);
        System.out.println(t.getTemperatura());
        t.cambiarMedicion();
        System.out.println(t.getTemperatura());
        System.out.println("-----------------------------------------------------");
        
        //Producto
        Producto pr = new Producto();
        pr.setPrecio(200);
        pr.setStock(2);
        pr.aplicarDescuento(15);
        System.out.println(pr.getPrecio());
        pr.realizarVenta();
        System.out.println(pr.getStock());
        pr.realizarVenta();
        System.out.println(pr.getStock());
        pr.realizarVenta();
        System.out.println("-----------------------------------------------------");
        
        //Pelota
        Pelota pt1 = new Pelota();
        Pelota pt2 = new Pelota();
        pt1.setCircunferencia(31.42);
        pt2.setCircunferencia(37.70);
        pt1.compararCircunferencia(pt1.getCircunferencia(), pt2.getCircunferencia());
        pt2.desinflarPelota();
        System.out.println(pt2.getCircunferencia());
        pt1.compararCircunferencia(pt1.getCircunferencia(), pt2.getCircunferencia());
        System.out.println("-----------------------------------------------------");
        
        //Reloj
        Reloj rj = new Reloj();
        rj.setHora(24);
        rj.setHora(23);
        rj.setMinutos(60);
        rj.setMinutos(59);
        rj.setSegundos(60);
        rj.setSegundos(59);
        System.out.println(rj.getHora() + ":" + rj.getMinutos() + ":" + rj.getSegundos());
        rj.avanzarTiempo();
        System.out.println(rj.getHora() + ":" + rj.getMinutos() + ":" + rj.getSegundos());
        rj.avanzarTiempo();
        System.out.println(rj.getHora() + ":" + rj.getMinutos() + ":" + rj.getSegundos());        
    }
    
}
