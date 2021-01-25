package beginner;

import java.util.Scanner;

public class URI_2718_Christmas_Lights {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max, count, len;
        int n = sc.nextInt();
        while (n-- > 0) {

            long x = sc.nextLong();
            max = 0;
            count = 0;

            while(x > 0){
                if (x % 2 == 1) {
                    count++;
                } else {
                    if (count > max) {
                        max = count;
                    }
                    count = 0;
                }
                x /= 2;
            }
            count = (max > count)? max: count;
            System.out.println(count);
        }
    }
}