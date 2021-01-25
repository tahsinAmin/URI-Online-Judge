package beginner;

import java.text.DecimalFormat;
import java.util.Scanner;

public class URI_2757_Input_And_Output_Of_Integers{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        DecimalFormat nF = new DecimalFormat("#0000000000");
        DecimalFormat nF2 = new DecimalFormat("#000000000");
        System.out.println("A = " + a + ", B = " + b + ", C = " + c);

        System.out.printf("A = %10s, B = %10s, C = %10s\n", a, b, c);
        if (a < 0) {
            System.out.println("A = " + nF2.format(a) + ", B = " + nF.format(b) + ", C = " + nF.format(c));
        } else {
            System.out.println("A = " + nF.format(a) + ", B = " + nF.format(b) + ", C = " + nF.format(c));
        }
        System.out.printf("A = %-10s, B = %-10s, C = %-10s\n", a, b, c);
    }

}
