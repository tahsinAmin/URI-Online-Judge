import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class URI2023TheLastGoodKid {
    public static void main(String[] args) throws IOException {
        String nome;
        String aux = "\0";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while ((nome = br.readLine()) != null) {
            if (nome.compareToIgnoreCase(aux) > 0) {
                aux=nome;
            }
        }
        System.out.println(aux);
    }
}