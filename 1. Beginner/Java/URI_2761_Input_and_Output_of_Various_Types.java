package beginner;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;

public class URI_2761_Input_and_Output_of_Various_Types {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        DecimalFormat nF = new DecimalFormat("#0.000000");
        while (sc.hasNext()) {
            String s = sc.nextLine();
            String splitA[] = s.split(" ");
            int a = Integer.parseInt(splitA[0]);
            Float b = Float.parseFloat(splitA[1]);
            char c = splitA[2].charAt(0);

            String phrase = s.substring(s.indexOf("" + c) + 2, s.length());

            System.out.printf("%s%s%s%s\n", a, nF.format(b), c, phrase);
            System.out.println(a + "\t" + nF.format(b) + "\t" + c + "\t" + phrase);
            System.out.printf("%10s%10s%10s%10s\n", a, nF.format(b), c, phrase);
        }
    }
}