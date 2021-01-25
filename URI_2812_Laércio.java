import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

//TODO https://www.urionlinejudge.com.br/judge/en/problems/view/2812
// URI_2812_Laércio
// line 32

public class URI_2812_Laércio {
    static int x, i, j, mid, size;
    static int[] a, newArray;
    public static void main(String[] args)throws IOException {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        while(n-- > 0){
            x = sc.nextInt();
            a = new int[x];

            for (int i = 0; i < x; i++) {
                a[i] = sc.nextInt();
            }

            Arrays.sort(a);

            i = 0;
            j = x-1;

            newArray = new int[x];
            size = 0;

            mid = (x/2);
            while(j >= mid){
                if (a[j]%2 == 1){
                    newArray[size] = a[j];
                    size++;
                    goToI();
                }
                j--;
            }
            goToI();

            for (int i = 0; i < size; i++){
                System.out.print(newArray[i]);
                if(i+1 != size){
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    private static void goToI() {
        while(i < mid) {
            if (a[i]%2 == 1) {
                newArray[size] = a[i];
                size++;
                i++;
                return;
            }
            i++;
        }
    }
}