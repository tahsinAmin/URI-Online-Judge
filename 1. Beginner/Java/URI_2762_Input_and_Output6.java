package beginner;

import java.util.Scanner;

public class URI_2762_Input_and_Output6{

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double d = sc.nextDouble();
        String sD = Double.toString(d);
        int dotIndex = sD.indexOf(".");
        String alt = sD.substring(dotIndex + 1, sD.length()) + "." + sD.substring(0, dotIndex);
        double nD = Double.parseDouble(alt);

        System.out.print(nD);
        if (alt.endsWith("0") && alt.startsWith("0")) {
            System.out.println("");
        } else if (alt.endsWith("0")) {
            System.out.println("0");
        } else {
            System.out.println("");
        }
    }
}
