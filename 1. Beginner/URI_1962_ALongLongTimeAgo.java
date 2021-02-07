package beginner;

import java.util.Scanner;

public class URI_1962_ALongLongTimeAgo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        while(n-- > 0){
            int x = sc.nextInt();
            if (x >=2015){
                System.out.println(x - 2014 + " A.C.");
            }else{
                System.out.println(2015 - x + " D.C.");
            }
        }
    }
}