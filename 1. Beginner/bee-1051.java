import java.io.IOException;
 
import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {
     public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        float s = sc.nextFloat();
        DecimalFormat numberFormat = new DecimalFormat("#.00");
        if(s > 2000.00){
            if(s > 3000.00){
                if(s > 4500.00)System.out.println("R$ " + numberFormat.format((float) ((1000*0.08)+ (1500*0.18) + ((s-4500)*0.28))));
                else System.out.println("R$ " + numberFormat.format((float) ((1000*0.08)+ ((s-3000)*0.18))));
            }else System.out.println("R$ " + numberFormat.format((float) ((s - 2000)*0.08)));
        }else System.out.println("Isento");
    }
}