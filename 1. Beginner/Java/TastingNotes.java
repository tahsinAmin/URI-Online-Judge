package beginner;

import java.util.Scanner;

public class TastingNotes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n >= 86 && n <=100)
            System.out.println("A");
        else if (n >= 61 && n <=85)
            System.out.println("B");
        else if (n >= 36 && n <=60)
            System.out.println("C");
        else if (n >= 1 && n <=35)
            System.out.println("D");
        else
            System.out.println("E");
    }
}
