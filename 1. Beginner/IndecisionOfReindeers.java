package beginner;

import java.util.Scanner;

public class IndecisionOfReindeers {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String []a = {"Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen","Rudolph"};

        int sum = 0;
        for (int i = 0; i< 9; i++){
            sum+= sc.nextInt();
        }
//        System.out.println(sum);
        if (sum%9 == 0){
            System.out.println(a[8]);
        }else{
            System.out.println(a[sum%9 -1]);
        }
    }
}