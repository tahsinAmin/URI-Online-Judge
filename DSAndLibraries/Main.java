package DSAndLibraries;

import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int tabs = sc.nextInt();
        int actions = sc.nextInt();
        String s;
        for (int i = 0; i < actions; i++) {
            s = sc.next();
            if (s.equals("fechou")) tabs++;
            else tabs--;
        }
        System.out.println(tabs);
    }
}