package beginner;

import java.text.DecimalFormat;
import java.util.Scanner;

public class ArrayFill3 {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        double a[] = new double [100];
        DecimalFormat numberFormat = new DecimalFormat("#0.0000");

        double n = sc.nextDouble();
        for(int i = 0; i< a.length; i++, n/=2.0){
            a[i] = n;
            System.out.printf("N[%d] = %.4f\n", i, a[i]);
        }
    }
}