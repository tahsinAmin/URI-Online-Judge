package beginner;

import java.util.Scanner;

public class Tachograph {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0 ;
        String[] splitA;
        sc.nextLine();
        for (int i = 0; i< n; i++) {
            splitA= sc.nextLine().split(" ");
            sum+= (Integer.parseInt(splitA[0]) * Integer.parseInt(splitA[1]));
        }
        System.out.println(sum);
    }
}
