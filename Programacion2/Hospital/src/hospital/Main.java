package hospital;

import javafx.application.Application;
import javafx.stage.Stage;
import hospital.model.HospitalData;
import hospital.view.MainMenu;
import javafx.scene.Scene;
       
public class Main extends Application {
    public static void main(String[] args) {
        launch(args);
    }
    
    @Override
    public void start(Stage stage) {
        HospitalData.cargarDatosDemo();
        
        MainMenu menu = new MainMenu(stage);
        Scene scene = new Scene(menu.getRoot(),400,300);
        stage.setTitle("Hospital Manager");
        stage.setScene(scene);
        stage.show();
    } 
    
}

