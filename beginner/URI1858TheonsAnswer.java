package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI1858TheonsAnswer {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int min = 21, minIndex = 0;

        for (int i = 1; i <= num; i++) {
            int n = sc.nextInt();

            if (min > n) {
                min = n;
                minIndex = i;
            }
        }
        System.out.println(minIndex);
    }
}