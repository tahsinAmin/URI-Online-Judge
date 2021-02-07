package beginner;

import java.util.Scanner;

public class URI_2162_PeaksAndValleys {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        boolean flag = true;
        if (n == 2) {
            flag = (a[0] != a[1]);
        }else{
            for (int i = 1; i < n - 1; i++) {
                if (i > 0 && i < n) {
                    if (a[i] == a[i - 1]) {
                        flag = false;
                        break;
                    } else if (((a[i] > a[i - 1]) && (a[i] > a[i + 1])) || ((a[i] < a[i - 1]) && (a[i] < a[i + 1]))) {
                        flag = true;
                    } else {
                        flag = false;
                    }
                }
            }
        }

        int count = (flag) ? 1 : 0;
        System.out.println(count);
    }
}