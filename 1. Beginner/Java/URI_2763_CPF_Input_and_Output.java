package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2763_CPF_Input_and_Output{

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        System.out.println(s.substring(0, 3) + "\n" + s.substring(4, 7) + "\n" + s.substring(8, 11) + "\n" + s.substring(12));
    }
}
