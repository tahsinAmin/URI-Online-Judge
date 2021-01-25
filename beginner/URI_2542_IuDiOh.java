package beginner;

import java.util.Scanner;

public class URI_2542_IuDiOh {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()){
            int n = sc.nextInt();
            int m = sc.nextInt();
            int l = sc.nextInt();
            int[][] marcos = new int[m][n];
            int[][] leonard = new int[l][n];

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    marcos[i][j] = sc.nextInt();
                }
            }

            for (int i = 0; i < l; i++) {
                for (int j = 0; j < n; j++) {
                    leonard[i][j] = sc.nextInt();
                }
            }

            int cM = sc.nextInt()  - 1;
            int cL = sc.nextInt() - 1;

            int a = sc.nextInt() - 1;

            int result = marcos[cM][a] - leonard[cL][a];

            String s = (result > 0) ? "Marcos" : (result < 0) ? "Leonardo" : "Empate";
            System.out.println(s);
        }
    }
}