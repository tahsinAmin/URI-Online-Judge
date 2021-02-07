package beginner;

import java.util.Scanner;

public class Balloon_of_Honor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char c = sc.next().charAt(0);
        int i = (int)c;
        System.out.println(i - 64);
    }
}
