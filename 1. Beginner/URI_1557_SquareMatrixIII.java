package beginner;
import java.util.Scanner;
public class URI_1557_SquareMatrixIII {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        while (m != 0) {
            int[][] a = new int[m][m];
            int x, y;

            x= 1;
            for (int row = 1;row <= m; row++){
                y = x;
                for (int column = 1; column<= m; column++){
                    a[row-1][column-1] = y;
                    y*=2;
                }
                x*=2;
            }

            int t = String.valueOf(a[m-1][m-1]).length();

            for (int row = 1; row <= m; row++) {
                for (int column = 1; column <= m; column++) {
                    System.out.printf("%" + t + "d", a[row-1][column-1]);
                    if (column < m){
                        System.out.print(" ");
                    }else{
                        System.out.println();
                    }
                }
            }
            System.out.println();
            m= sc.nextInt();
        }
    }
}