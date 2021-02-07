package beginner;
import java.io.IOException;
import java.util.Scanner;

public class SummingConsecutiveIntegers {
    public static void main(String[]args) throws IOException{
        Scanner sc = new Scanner(System.in);

        int a, n;
        int result= 0;
        a = sc.nextInt();

        do{
            n = sc.nextInt();
        }while(n <= 0);

        for(; n>0;n--){
            result += a;
            a++;
        }
        System.out.println(result);
    }
}