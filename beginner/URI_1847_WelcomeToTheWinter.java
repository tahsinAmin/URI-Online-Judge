package beginner;

import java.util.Scanner;

public class URI_1847_WelcomeToTheWinter {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        double aToB = (b - a) / 5.0;
        double bToC = (c - b) / 5.0;

        if(a==b && b==c) System.out.println(":(");

        else if (b >= a) {
            if (bToC >= aToB) System.out.println(":)");
            else System.out.println(":(");
        } else {
            if (bToC > aToB) System.out.println(":)");
            else System.out.println(":(");
        }
    }
}