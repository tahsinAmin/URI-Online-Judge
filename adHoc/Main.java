package adHoc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Main {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int cases = 0;
        int n = Integer.parseInt(in.readLine());
        while (n-- > 0) {
            String split[] = in.readLine().split(" ");
            int men = Integer.parseInt(split[0]);
            int skips = Integer.parseInt(split[1]);

            System.out.println("Value of men and skips: " + men + " " + skips);

            int sumOfNTerms = ((men + 1) * (men)) / 2;
            int a[] = new int[men];
            int size = men;
            int skipCount = 0;

            for (int i = 0; size != 1; i = (i + 1) % men) {
                if (a[i] == 0) {
                    skipCount++;
                    if (skipCount == skips) {
                        size--;
                        a[i] = 1;
                        skipCount = 0;
                        sumOfNTerms -= i;
                    }
                }
            }
            out.println("Case " + ++cases + ": " + ((sumOfNTerms - men) + 1));
        }
        out.close();
    }
}

