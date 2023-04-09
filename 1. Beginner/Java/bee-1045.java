import java.io.IOException;
 
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        String splitA[];
        String line = sc.nextLine();
        splitA = line.split(" ");
        double A = Double.parseDouble(splitA[0]);
        double B = Double.parseDouble(splitA[1]);
        double C = Double.parseDouble(splitA[2]);
        
        if(B >C){
            if(A > B){}
            else{
                double temp = B;
                B = A;
                A = temp;
            }
        }else{
            if(A > C){}
            else{
                double temp = C;
                C = A;
                A = temp;
            }
        }
        
        for(int i = 0; i <1; i++){
            if( A >= (B + C)){
                System.out.println("NAO FORMA TRIANGULO");
                break;
            }
            if (Math.pow(A,2) == (Math.pow(B,2) + Math.pow(C,2))) System.out.println("TRIANGULO RETANGULO");
            else if (Math.pow(A,2) > (Math.pow(B,2) + Math.pow(C,2))) System.out.println("TRIANGULO OBTUSANGULO");
            else System.out.println("TRIANGULO ACUTANGULO");
            
            if(A == B && B== C){
                System.out.println("TRIANGULO EQUILATERO");
                break;
            }

            if((B == A ) || ( A == C) || (C == B)) System.out.println("TRIANGULO ISOSCELES");
        }
    }
}
