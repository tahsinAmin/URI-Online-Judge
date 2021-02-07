package beginner;

import java.util.Scanner;

public class URI_1958_Scientific_Notation {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n = sc.nextDouble();
        System.out.println(String.format((String.valueOf(n).startsWith("-") ? "" : "+") + "%.4E", n));
    }
}