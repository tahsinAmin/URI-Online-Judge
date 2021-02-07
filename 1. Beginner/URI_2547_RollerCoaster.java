package beginner;

import java.util.Scanner;

public class URI_2547_RollerCoaster {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            int n = sc.nextInt();
            int aMin = sc.nextInt();
            int aMax = sc.nextInt();

            int count = 0;

            for (int i = 0; i < n; i++) {
                int height = sc.nextInt();
                if(height >= aMin && height <= aMax) count++;
            }
            System.out.println(count);
        }
    }
}