import java.text.DecimalFormat;
import java.util.Scanner;

public class URI_2758_Floating_Number_Input_and_Output {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        float a = sc.nextFloat();
        float b = sc.nextFloat();
        double c = sc.nextDouble();
        double d = sc.nextDouble();

        System.out.format("A = %.6f, B = %.6f\n" +
                "C = %.6f, D = %.6f\n", a, b, c, d);

        System.out.format("A = %.1f, B = %.1f\n" +
                "C = %.1f, D = %.1f\n", a, b, c, d);

        System.out.format("A = %.2f, B = %.2f\n" +
                "C = %.2f, D = %.2f\n", a, b, c, d);

        System.out.format("A = %.3f, B = %.3f\n" +
                "C = %.3f, D = %.3f\n", a, b, c, d);

        System.out.println(String.format("A = %.3E, B = %.3E\nC = %.3E, D = %.3E", a, b, c, d));

        DecimalFormat df = new DecimalFormat("0");
        System.out.println("A = " + df.format(a) + ", B = " + df.format(b));
        System.out.println("C = " + df.format(c) + ", D = " + df.format(d));

    }
}