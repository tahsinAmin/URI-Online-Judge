import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
         String splitA[];
        
        String input = sc.nextLine();
        splitA = input.split(" ");
        int x = Integer.parseInt(splitA[0]);
        int y = Integer.parseInt(splitA[1]);
        
        if(y%x == 0 || x%y ==0) System.out.println("Sao Multiplos");
        else System.out.println("Nao sao Multiplos");
    }
}