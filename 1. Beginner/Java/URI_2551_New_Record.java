package beginner;

import java.util.Scanner;

public class URI_2551_New_Record {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            int n = sc.nextInt();
            double a[][] = new double[n][2];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < 2; j++) {
                    a[i][j] = sc.nextInt();
                }
            }

            double averageSpeed = 0;
            int best = 1;

            for (int i = 0; i < n; i++) {
                if (a[i][1] / a[i][0] > averageSpeed) {
                    best = i + 1;
                    averageSpeed = a[i][1] / a[i][0];
                    System.out.println(best);
                }
            }
        }
    }
}