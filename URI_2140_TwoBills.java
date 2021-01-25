import java.io.IOException;
import java.util.Scanner;


public class URI_2140_TwoBills {

    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        while (true) {
            int price = leitor.nextInt();
            int pays = leitor.nextInt();
            int difference = pays - price;
            int[] available = {2, 5, 10, 20, 50, 100};
            boolean isItPossible = false;

            if (price == 0 && pays == 0) break;

            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 6; j++) {
                    if (difference - available[j] == available[i]) isItPossible = true;
                }
            }

            if (isItPossible) System.out.println("possible");
            else System.out.println("impossible");
        }
    }

}