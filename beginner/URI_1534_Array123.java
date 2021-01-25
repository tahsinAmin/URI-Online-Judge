package beginner;

import java.util.Scanner;

public class URI_1534_Array123 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            int m = sc.nextInt();

            int[][] a = new int[m][m];
            a = putValue(m, m, 0, a);
            for (int row = 0; row < m; row++) {
                for (int column = 0; column < m; column++) {
                    System.out.print(a[row][column]);
                }
                System.out.println("");
            }
        }
    }

    public static int[][] putValue(int m, int n, int c, int a[][]) {

        if ((m - n) == m) {
            return a;
        } else {

            int row = m - n, column = m - n;

            for (; column <= m - 1; column++) {
                if (column == m - c - 1) {
                    a[row][column] = 2;
                } else {
                    a[row][column] = 3;
                }
            }

            column = row;
            for (; row <= m - 1; row++) {
                if (row == m - c - 1) {
                    a[row][column] = 2;
                } else if (row == m - n) {
                    a[row][column] = 1;
                } else {
                    a[row][column] = 3;
                }
            }
            return putValue(m, n - 1, c = c + 1, a);
        }
    }
}