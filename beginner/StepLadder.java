package beginner;

import java.util.Scanner;

public class StepLadder {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int [] a = new int[n];

        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }

        int count;
        count = 0;
        if (n==1) count= 1;

        int same = -256;
        for(int i = 0; i<n- 1;i++){
            int diff = a[i] - a[i+1];
            if (diff != same){
                count++;
                same = diff;
            }else{
            }
        }
        System.out.println(count);
    }
}