package Math;

import java.util.Scanner;

public class PascalsTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i = 0; i< n; i++) {
            int x = sc.nextInt();
            int sum=0;
            for (int j = x-1; j >-1;j--){
                sum+=Math.pow(2,j);
            }
            System.out.println(sum);
        }
    }
}
