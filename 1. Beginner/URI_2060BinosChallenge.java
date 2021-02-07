package beginner;

import java.util.Scanner;

public class URI_2060BinosChallenge {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count2 = 0, count3 = 0, count4 = 0, count5 = 0;
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < arr.length; i++) {
            int a = arr[i];
            if (a % 2 == 0) {
                count2++;
            }
            if (a % 3 == 0) {
                count3++;
            }
            if (a % 4 == 0) {
                count4++;
            }
            if (a % 5 == 0) {
                count5++;
            }
        }
        System.out.printf("%d Multiplo(s) de 2\n",count2);
        System.out.printf("%d Multiplo(s) de 3\n",count3);
        System.out.printf("%d Multiplo(s) de 4\n",count4);
        System.out.printf("%d Multiplo(s) de 5\n",count5);
    }
}