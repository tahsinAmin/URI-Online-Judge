package beginner;

import java.util.Scanner;

public class URI_2235_Walking_in_Time {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        String s = ((a == b) || (a == c) || (b == c) || (a + c) == b || (b + c) == a || ((a + b) == c)) ? "S" : "N";
        System.out.println(s);
    }
}