package beginner;

import java.util.Scanner;

public class The_Fellowship_of_the_Ring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = "XHEAM";
        int a2[] = new int[5];
        int num = sc.nextInt();
        sc.nextLine();

        for (int i =0; i< num; i++) {
            String splitA[] = sc.nextLine().split(" ");
            a2[a.indexOf(splitA[1])]++;
        }
        System.out.println(a2[0] + " Hobbit(s)");
        System.out.println(a2[1] + " Humano(s)");
        System.out.println(a2[2] + " Elfo(s)");
        System.out.println(a2[3] + " Anao(s)");
        System.out.println(a2[4] + " Mago(s)");
    }
}
