package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2780_Robot_Basketball {

    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        if (i <= 800) {
            System.out.println("1");
        }
        if (i > 800 && i <= 1400) {
            System.out.println("2");
        }
        if (i > 1400 && i <= 2000) {
            System.out.println("3");
        }
    }
}
