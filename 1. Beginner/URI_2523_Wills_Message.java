package beginner;

import java.util.Scanner;

public class URI_2523_Wills_Message {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, n;
        while (sc.hasNext()) {
            String s = sc.next();
            n = sc.nextInt();
            while(n-- > 0){
                x = sc.nextInt();
                System.out.print(s.charAt(x-1));
            }
            System.out.println();
        }
    }
}
