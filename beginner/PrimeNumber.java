package beginner;
import java.io.IOException;
import java.util.Scanner;

public class PrimeNumber{

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int flag = 0;

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            if (x<=1){
                System.out.printf("%d nao eh primo\n", x);
            }

            for (int j = 2; j< x; j++){
                if (x%j==0){
                    System.out.printf("%d nao eh primo\n", x);
                    flag= 1;
                    break;
                }
            }
            if(flag != 1){
                System.out.println(x + " eh primo");
            }else{
                flag = 0;
            }
        }
    }
}