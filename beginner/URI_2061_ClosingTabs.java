package beginner;
import java.io.IOException;
import java.util.Scanner;

public class URI_2061_ClosingTabs {

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
