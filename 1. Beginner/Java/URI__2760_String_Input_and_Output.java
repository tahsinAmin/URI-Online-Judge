package beginner;

import java.util.Scanner;

public class URI__2760_String_Input_and_Output {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        String c = sc.nextLine();

        System.out.println(a + b + c);
        System.out.println(b + c + a);
        System.out.println(c + a + b);
        if (a.length() > 10) {
            
            a = a.substring(0, 10);
        }if (b.length() > 10) {
            b = b.substring(0, 10);
        }if (c.length() > 10) {
            
            c = c.substring(0, 10);
        }
        System.out.println(a + b + c);
    }
}
