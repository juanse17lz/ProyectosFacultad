package hospital.view;

import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class MainMenu {
    private VBox root;
    
    public MainMenu(Stage stage) {
        root = new VBox(20);
        root.setStyle("-fx-padding: 30; -fx-aligment: center");
        
        Button btnPacientes = new Button("Gestionar Pacientes");
        Button btnDoctores = new Button("Gestionar Doctores");
        Button btnTurnos = new Button("Gestionar Turnos");
        
        btnPacientes.setOnAction(e -> abrirVentana(stage, new PacientesView(stage).getRoot(),"Portal Pacientes"));
        //btnDoctores.setOnAction(e -> abrirVentana(stage, new DoctoresView(stage).getRoot(), "Portal Doctores"));
        //btnTurnos.setOnAction(e -> abrirVentana(stage, new TurnosView(stage).getRoot(),"Portal Turnos"));
        
        root.getChildren().addAll(btnPacientes, btnDoctores, btnTurnos);
    }
    
    public Parent getRoot() {
        return root;
    }
    
    public void abrirVentana(Stage stage, VBox contenido, String titulo) {
        Stage nuevo = new Stage();
        nuevo.setTitle(titulo);
        nuevo.setScene(new Scene(contenido, 600, 400));
        nuevo.show();
    }
    
}
