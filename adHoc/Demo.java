package adHoc;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Demo {
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int cases = 0;
        int n = sc.nextInt();
        while (n-- > 0) {
            int men = sc.nextInt();
            int skips = sc.nextInt();

            out.println("Case " + ++cases + ": " + (josephus(men, skips) + 1));
        }
        out.close();
    }

    private static int josephus(int men, int skips) {
        int ans = 0;
        for (int i=2; i<=men; i++){
            ans= (ans + skips)% i;
        }
        return ans;
    }
}