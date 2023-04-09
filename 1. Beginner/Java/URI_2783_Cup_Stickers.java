package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2783_Cup_Stickers {

    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();int c = sc.nextInt();int m = sc.nextInt();
        int count = 0;


        int[] cA = new int[c];int[] mA = new int[m];

        count = c;

        for (int i = 0; i< c; i++){
            cA[i] = sc.nextInt();
        }

        for (int i = 0; i< m; i++){
            mA[i] = sc.nextInt();
        }

        for (int i = 0; i< c; i++){
            for (int j = 0; j< m; j++){
                if (cA[i] == mA[j]){
                    count--;
                    break;
                }
            }
        }

        System.out.println(count);
    }
}
