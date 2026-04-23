package sistemadegestiondeexpedicionesespaciales;

import java.util.Scanner;

public class SistemaDeGestionDeExpedicionesEspaciales {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        GestorDeNaves agencia = new GestorDeNaves();
        
        int opcion;
        do {
            System.out.println("\n===== Sistema de Expediciones Espaciales =====\n");
            System.out.println("\n1) Agregar Nave Espacial");
            System.out.println("2) Eliminar Nave Espacial");
            System.out.println("3) Mostrar lista de Naves");
            System.out.println("4) Iniciar Exploracion de Naves");
            System.out.println("0) Salir del sistema\n");
            System.out.println("\nElige una opcion: ");
            
            opcion = sc.nextInt();
            sc.nextLine();
            
            switch(opcion) {
                case 1 -> {                                          
                    System.out.println("Elige el tipo de nave que quiere agregar: ");
                    System.out.println("1) Nave de Exploracion");
                    System.out.println("2) Carguero");
                    System.out.println("3) Crucero Estelar");
                    System.out.println("0) Volver al menu");
                    System.out.println("Elige una opcion: ");
                    int opcionNave = sc.nextInt();
                    sc.nextLine();
                    switch(opcionNave) {
                        case 1 -> {
                            System.out.println("Ingrese el nombre de la nave de exploracion: ");
                            String nombre = sc.nextLine();
                            System.out.println("Ingrese el año de lanzamiento: ");
                            int añoLanzamiento = sc.nextInt();
                            System.out.println("Ingrese la capacidad de la tripulacion: ");
                            int capacidadTripulacion = sc.nextInt();
                            System.out.println("Ingrese la mision de la nave (1-INVESTIGACION | 2-CONTACTO | 3-CARTOGRAFIA): ");
                            int opcionMision = sc.nextInt();
                            TipoMision mision;
                            switch(opcionMision) {
                                case 1 -> mision = TipoMision.INVESTIGACION;
                                case 2 -> mision = TipoMision.CONTACTO;
                                case 3 -> mision = TipoMision.CARTOGRAFIA;
                                default -> {
                                    System.out.println("Opcion invalida. Por defecto se asignara INVESTIGACION.");
                                    mision = TipoMision.INVESTIGACION;
                                }
                            }
                            try {
                                NaveExploracion nuevaNave = new NaveExploracion(nombre,capacidadTripulacion,añoLanzamiento,mision);
                                agencia.agregarNave(nuevaNave);
                            } catch (NaveDuplicadaExcepcion e) {   
                                System.out.println("Error: " + e.getMessage());
                            }
                        }
                        case 2 -> {
                            System.out.println("Ingrese el nombre de la nave carguera: ");
                            String nombre = sc.nextLine();
                            System.out.println("Ingrese el año de lanzamiento: ");
                            int añoLanzamiento = sc.nextInt();
                            System.out.println("Ingrese la capacidad de la tripulacion: ");
                            int capacidadTripulacion = sc.nextInt();
                            System.out.println("Ingrese la capacidad de carga de la nave (Entre 100 y 500 toneladas): ");
                            int capacidadCarga = sc.nextInt();
                            if (capacidadCarga < 100) {
                                System.out.println("La capacidad minima de carga es de 100 toneladas. Por defecto se asignaran 100 toneladas de carga.");
                                capacidadCarga = 100;                                
                            } else if (capacidadCarga > 500) {
                                System.out.println("La capacidad maxima de carga es de 500 toneladas. Por defecto se asignaran 500 toneladas de carga.");
                                capacidadCarga = 500;
                            }
                            try {
                                Carguero nuevaNave = new Carguero(capacidadCarga,nombre,capacidadTripulacion,añoLanzamiento);
                                agencia.agregarNave(nuevaNave);
                            } catch (NaveDuplicadaExcepcion e) {
                                System.out.println("Error: " + e.getMessage());
                            }
                        }
                        case 3 -> {
                            System.out.println("Ingrese el nombre del crucero estelar: ");
                            String nombre = sc.nextLine();
                            System.out.println("Ingrese el año de lanzamiento: ");
                            int añoLanzamiento = sc.nextInt();
                            System.out.println("Ingrese la capacidad de la tripulacion: ");
                            int capacidadTripulacion = sc.nextInt();
                            System.out.println("Ingrese la capacidad de pasajeros: ");
                            int capacidadPasajeros = sc.nextInt();
                            try {
                                CruceroEstelar nuevaNave = new CruceroEstelar(capacidadPasajeros,nombre,capacidadTripulacion,añoLanzamiento);
                                agencia.agregarNave(nuevaNave);
                            } catch (NaveDuplicadaExcepcion e) {
                                System.out.println("Error: " + e.getMessage());
                            }
                        }
                        case 0 -> {
                            System.out.println("Volviendo al menu: ");
                        }
                        default -> {
                            System.out.println("Opcion invalida. Volviendo al menu.");
                        }
                    }
                }
                case 2 -> {
                    System.out.println("Ingrese el nombre de la nave que desea eliminar: ");
                    String nombre = sc.nextLine();
                    System.out.println("Ingrese el año de lanzamiento de la nave que desea eliminar: ");
                    int añoLanzamiento = sc.nextInt();
                    agencia.eliminarNave(nombre, añoLanzamiento);
                }
                case 3 -> {
                    agencia.mostrarNaves();
                }
                case 4 -> {
                    System.out.println("Ingrese el nombre de la nave de exploracion: ");
                    String nombre = sc.nextLine();
                    System.out.println("Ingrese el año de lanzamiento de la nave de exploracion: ");
                    int añoLanzamiento = sc.nextInt();
                    Nave naveExploracion = agencia.buscarNave(nombre, añoLanzamiento);
                    if (naveExploracion == null) {
                        System.out.println("No se puede iniciar la exploracion.");
                    } else {
                        agencia.iniciarExploracion(naveExploracion);
                    }
                }
                case 0 -> {
                    System.out.println("Saliendo del programa.");
                }
                default -> {
                    System.out.println("Opcion invalida.");
                }
            }
        } while(opcion != 0);
    }    
}