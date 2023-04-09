import java.io.IOException;
 
import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner (System.in);
        float a [] = new float[6];
        for(int i = 0; i<6; i++){
            a[i] = sc.nextFloat();
        }
        int count = 0;
        for(int i = 0; i<6; i++){
            if(a[i]> 0) count++;
        }
        System.out.println(count + " valores positivos");
    }
}