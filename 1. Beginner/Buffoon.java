package beginner;

import java.util.Scanner;

public class Buffoon {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int s = sc.nextInt();
        sc.nextLine();
        int max = 0;
        for (int i = 0; i < n-1; i++) {
            int score =sc.nextInt();
            if(max < score) {
                max = score;
            }
        }

        if ( s >= max) {
            System.out.println("S");
        }else {
            System.out.println("N");
        }
    }
}
