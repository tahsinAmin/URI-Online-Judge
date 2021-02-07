package beginner;

import java.util.Arrays;
import java.util.Scanner;

public class URI_2534_General_Exam {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x, n;
        int[] citizens, positions;


        while (sc.hasNext()) {
            n = sc.nextInt();
            x = sc.nextInt();

            citizens = new int[n];
            positions = new int[x];

            for (int i = 0; i< n; i++){
                citizens[i] = sc.nextInt();
            }

            Arrays.sort(citizens);

            for (int i = 0; i< x; i++){
                positions[i] = sc.nextInt();
            }

            for(int i = 0; i< x; i++){
                System.out.println(citizens[citizens.length - positions[i]]);
            }
        }
    }
}