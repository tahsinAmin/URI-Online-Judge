package beginner;

import java.util.Scanner;

public class HourOfARun {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();
        int n = sc.nextInt();

        int total = v*n;

        int i = 10;
        for(; i<= 80; i+=10) {
            System.out.print((int)Math.ceil(((i * total) / 100.0)) + " ");
        }
        System.out.println((int)Math.ceil(((i * total) / 100.0)));
    }
}
