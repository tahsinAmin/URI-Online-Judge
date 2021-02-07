package beginner;

import java.util.Scanner;

public class How_Much_Cassava {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a [] = {300,1500,600, 1000, 150};

        int sum = 225;
        for (int i =0; i< 5; i++) {
            sum+= sc.nextInt() * a[i];
        }
        System.out.println(sum);
    }
}
