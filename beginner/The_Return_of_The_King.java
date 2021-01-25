package beginner;

import java.util.Scanner;

public class The_Return_of_The_King {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String splitA[] = sc.nextLine().split(" ");

        int n = Integer.parseInt(splitA[0]);
        int val = Integer.parseInt(splitA[1]);

        String a1[] = new String[n];
        int a2[] = new int[n];
//        System.out.println("Time to take " + n + " number of rumes.");

        for (int i =0; i< n; i++){
            splitA = sc.nextLine().split(" ");
            a1[i] = splitA[0];
            a2[i] = Integer.parseInt(splitA[1]);
        }
//        System.out.println("time to take number of rumes to recite....");
        n = sc.nextInt();
        int reciteVal = 0;
//        System.out.println("time to give " + n + " number of rumes...");
        sc.nextLine();
        splitA = sc.nextLine().split(" ");
        for (int i =0; i< n; i++) {
            for (int j = 0; j<a1.length; j++) {
//                System.out.println("value of a1 and split[" + i+"]  is " + a1[j] + " & " + splitA[i]);
                if (a1[j].equals(splitA[i])) {
                    reciteVal+= a2[j];
                }
            }
        }
        System.out.println(reciteVal);
        if (reciteVal<val) {
            System.out.println("My precioooous");
        }else {
            System.out.println("You shall pass!");
        }

    }
}
