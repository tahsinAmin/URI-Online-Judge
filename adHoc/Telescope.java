package adHoc;

import java.util.Scanner;

public class Telescope {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int telArea = sc.nextInt();
        int n= sc.nextInt();
        int count = 0;

        sc.nextLine();
        for (int i = 0; i< n; i++) {
            int t = sc.nextInt();

            if((t*telArea) >= 40000000) {
                count++;
            }
        }
        System.out.println(count);
    }
}
