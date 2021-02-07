package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2764_Date_Input_and_Output{

    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        System.out.println(s.substring(3, 5) + "/" + s.substring(0, 2) + "/" + s.substring(6));
        System.out.println(s.substring(6) + "/" + s.substring(3, 5) + "/" + s.substring(0, 2));
        System.out.println(s.substring(0, 2) + "-" + s.substring(3, 5) + "-" + s.substring(6));
    }
}
