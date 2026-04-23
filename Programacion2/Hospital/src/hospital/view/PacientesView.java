package hospital.view;

import hospital.model.HospitalData;
import hospital.model.Paciente;
import javafx.beans.property.SimpleStringProperty;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class PacientesView {
    private VBox root;
    
    public PacientesView(Stage stage) {
        root = new VBox(10);
        root.setStyle("-fx-padding: 20");
        
        TextField txtDni = new TextField();
        txtDni.setPromptText("DNI");
        TextField txtNombre = new TextField();
        txtNombre.setPromptText("Nombre");
        TextField txtApellido = new TextField();
        txtApellido.setPromptText("Apellido");
        TextField txtObraSocial = new TextField();
        txtObraSocial.setPromptText("Obra Social");
                
        Button btnAgregar = new Button("Agregar");                
        Button btnEliminar = new Button("Eliminar");
        
        HBox form = new HBox(10,txtDni,txtNombre,txtApellido,txtObraSocial,btnAgregar,btnEliminar);
        form.setStyle("-fx-aligment: center");

        TableView<Paciente> tabla = new TableView<>(HospitalData.getPacientes());        
        TableColumn<Paciente, String> cDni = new TableColumn<>("DNI");
        TableColumn<Paciente, String> cNombre = new TableColumn<>("Nombre");
        TableColumn<Paciente, String> cApellido = new TableColumn<>("Apellido");
        TableColumn<Paciente, String> cObraSocial = new TableColumn<>("Obra Social");
        
        cDni.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getDni()));
        cNombre.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getNombre()));
        cApellido.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getApellido()));
        cObraSocial.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getObraSocial()));
        
        tabla.getColumns().addAll(cDni,cNombre,cApellido,cObraSocial);
        tabla.setPrefHeight(250);
        
        btnAgregar.setOnAction(e -> {
                if (txtDni.getText().isEmpty() || txtNombre.getText().isEmpty()) 
                    return;
                HospitalData.getPacientes().add(new Paciente(txtDni.getText(), txtNombre.getText(), txtApellido.getText(),txtObraSocial.getText()));
                txtDni.clear();
                txtNombre.clear();
                txtApellido.clear();
                txtObraSocial.clear();
        });
        
        btnEliminar.setOnAction(e -> {
            Paciente sel = tabla.getSelectionModel().getSelectedItem();
            if (sel != null) HospitalData.getPacientes().remove(sel);
        });
        
        root.getChildren().addAll(form, tabla, btnEliminar); 
    }
    
    public VBox getRoot() { return root; }
}
