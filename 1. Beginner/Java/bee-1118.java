import java.text.DecimalFormat;
import java.util.LinkedList;
import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        LinkedList<String> l =  new LinkedList<String>();
        DecimalFormat numberFormat = new DecimalFormat("#0.00"); 
        float grades[] = new float[2];
        int r = 0;
        
        do{
            int counter = 0, g = 0;
            for(; counter< grades.length;){
               float inp = sc.nextFloat();
               if (inp <= 10 && inp >= 0){
                   grades[counter] = inp;
                   counter++;
               }else g++;
            }
            for(int i = 0; i< g; i++){
                System.out.println("nota invalida");
            }
            System.out.println("media = " + numberFormat.format((grades[0]+grades[1])/2));
            for(;counter>=0; counter++){
                System.out.println("novo calculo (1-sim 2-nao)");
                r = sc.nextInt();
                if(r == 1 || r ==2) break;
            }
        }while(r == 1);
    }
}