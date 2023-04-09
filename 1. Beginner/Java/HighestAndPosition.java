package beginner;
import java.io.IOException;
import java.util.Scanner;

public class HighestAndPosition {
    public static void main(String[]args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int max = 0; int maxIndex=0; int a[] = new int[101];

        for (int i = 1; i< a.length; i++){
            a[i] = sc.nextInt();
            if (a[i]> max){
                max = a[i];
                maxIndex = i;
            }
        }
        System.out.println(max + "\n" + maxIndex);
    }
}