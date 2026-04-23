package hospital.model;

import java.time.LocalDateTime;

public class Turno {
    private Paciente paciente;
    private Doctor doctor;
    private LocalDateTime fechaHora;

    public Turno(Paciente paciente, Doctor doctor, LocalDateTime fechaHora) {
        this.paciente = paciente;
        this.doctor = doctor;
        this.fechaHora = fechaHora;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

    public LocalDateTime getFechaHora() {
        return fechaHora;
    }

    public void setFechaHora(LocalDateTime fechaHora) {
        this.fechaHora = fechaHora;
    }

    @Override
    public String toString() {
        return "Turno{" + "paciente=" + paciente + ", doctor=" + doctor + ", fechaHora=" + fechaHora + '}';
    }
    
}
