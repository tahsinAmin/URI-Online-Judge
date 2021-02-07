package beginner;

// TODO https://www.urionlinejudge.com.br/judge/en/problems/view/2168

import java.util.Scanner;

public class URI_2168_TwilightAtPortland {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[][] a = new int[n+1][n+1];

        for(int row = 0; row< a.length; row++){
            for(int column = 0; column< a.length; column++){
                a[row][column] = scanner.nextInt();
            }
        }
        
        int count=0;
        for(int row = 0; row< a.length-1; row++){

            for(int column = 0; column< a.length-1; column++){
                count += (a[row][column] == 1) ? 1 : 0 ;
                count += (a[row][column+1] == 1) ? 1 : 0 ;
                count += (a[row+1][column] == 1) ? 1 : 0 ;
                count += (a[row+1][column+1] == 1) ? 1 : 0 ;

                String s = (count>=2) ? "S" : "U";
                System.out.print(s);
                count=0;
            }
            System.out.println();
        }

    }
}