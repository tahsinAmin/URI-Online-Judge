package begineer;

import java.util.Arrays;
import java.util.Scanner;

public class URI_2779_Album_of_the_Cup{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int space = sc.nextInt();
        int purchase = sc.nextInt();
        int a[] = new int[purchase];

        for (int i = 0; i < purchase; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);
        int dif = 0;
        for (int i = 1; i < purchase; i++) {
            
            if (a[i] != a[i - 1]) {
                dif++;
                
            }
        }
        System.out.println(space - dif - 1);
    }
}
