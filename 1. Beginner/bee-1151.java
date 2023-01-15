import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        
        int x = sc.nextInt();
        int z;
        do{
            z = sc.nextInt();
        }while(z<=x);
        int sum = 0; int count = 0;
        for(int i = x; sum< z; i++){
            sum +=i;
            count++;
        }
        System.out.println(count);
    }
}