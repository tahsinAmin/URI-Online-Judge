package beginner;

import java.util.Scanner;

public class URI_2759_Input_and_Output_Character_2759 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);
        char b = sc.next().charAt(0);
        char c = sc.next().charAt(0);

        System.out.println("A = " + a + ", B = " + b + ", C = " + c);
        System.out.println("A = " + b + ", B = " + c + ", C = " + a);
        System.out.println("A = " + c + ", B = " + a + ", C = " + b);

    }
}