package beginner;

import java.util.Scanner;

public class TheStrikeStopsOrContinues {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0; String splitA[];
        sc.nextLine();
        for (int i = 0; i< n; i++) {
            splitA = sc.nextLine().split(" ");
            if (splitA[0].equals("G")) {
                sum-= Integer.parseInt(splitA[1]);
            }else if(splitA[0].equals("V")) {
                sum+= Integer.parseInt(splitA[1]);
            }
        }
        if (sum>=0) {
            System.out.println("The strike will stop.");
        }else{
            System.out.println("NO CUT, FIGHT!");
        }
    }
}
