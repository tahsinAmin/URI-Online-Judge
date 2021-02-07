package beginner;

import java.util.Scanner;

public class The_Two_Towers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String splitA[] = sc.nextLine().split(" ");
        int a= Integer.parseInt(splitA[0]);
        int b= Integer.parseInt(splitA[1]);
        int c= Integer.parseInt(splitA[2]);

        System.out.printf("%.2f" + System.lineSeparator(), (double)a/(b+c));
    }
}
