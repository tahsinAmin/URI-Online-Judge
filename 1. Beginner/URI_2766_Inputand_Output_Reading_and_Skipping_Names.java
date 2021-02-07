package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2766_Inputand_Output_Reading_and_Skipping_Names{

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String a[] = new String[10];
        for (int i = 0; i < 10; i++) {
            a[i] = sc.nextLine();
        }

        for (int i = 0; i < 10; i++) {
            if (i == 2 || i == 6 || i == 8) {
                System.out.println(a[i]);
            }
        }

    }
}
