import java.io.IOException;
 
import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
         String splitA[];
        
        String input = sc.nextLine();
        splitA = input.split(" ");
        int x = Integer.parseInt(splitA[0]);
        int y = Integer.parseInt(splitA[1]);
        int z = Integer.parseInt(splitA[2]);
                
        int copy[] = new int[3];
        copy[0] = x;
        copy[1] = y;
        copy[2] = z;       
        
        boolean flag = true;
        while (flag == true){
            flag = false;
            for(int i = 0; i< copy.length-1; i++){
                if(copy[i] > copy[i+1]){
                    int temp = copy[i];
                    copy[i] = copy[i+1];
                    copy[i+1] = temp;
                    flag = true;
                }
            }
        }
        for(int i = 0; i< copy.length; i++){
            System.out.println(copy[i]);
        }
        System.out.println();
        for(int i = 0; i< splitA.length; i++){
            System.out.println(splitA[i]);
        }
    }
}