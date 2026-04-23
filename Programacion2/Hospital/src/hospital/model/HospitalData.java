package hospital.model;

import javafx.collections.ObservableList;
import javafx.collections.FXCollections;

public class HospitalData {
    private static ObservableList<Paciente> pacientes = FXCollections.observableArrayList();
    private static ObservableList<Doctor> doctores = FXCollections.observableArrayList();
    private static ObservableList<Turno> turnos = FXCollections.observableArrayList();
   
    public static ObservableList<Paciente> getPacientes() { return pacientes;}
    public static ObservableList<Doctor> getDoctores() { return doctores;}
    public static ObservableList<Turno> getTurnos() { return turnos;}
    
    public static void cargarDatosDemo() {
        pacientes.addAll(
                new Paciente("30111222","Ana","Perez","OSDE"),
                new Paciente("28999888","Luis","Fernandez","IOMA")
        );
        doctores.addAll(
                new Doctor("M.1234","Carla","Ruiz","Cardiologia"),
                new Doctor("M.9876","Javier","Suarez", "Clinica Medica")
        );
    }
}
