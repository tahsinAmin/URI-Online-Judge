package beginner;

import java.util.Scanner;

public class URI_1961_JumpingFrog {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int jumpHeight = sc.nextInt(), numberOfPipes = sc.nextInt();

        int[] a = new int[numberOfPipes];
        for (int i = 0; i < numberOfPipes; i++) a[i] = sc.nextInt();

        String s = "YOU WIN";
        for (int i = 1; i < numberOfPipes; i++) {
            if ( a[i - 1] - a[i] < (-jumpHeight) || a[i - 1] - a[i] > jumpHeight) {
                s = "GAME OVER";
                break;
            }
        }
        System.out.println(s);
    }
}