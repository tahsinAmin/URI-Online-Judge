package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2765_Coming_Input_and_Output{

    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        int index = s.indexOf(",");
        System.out.println(s.substring(0, index) + "\n" + s.substring(index + 1));
    }

}
