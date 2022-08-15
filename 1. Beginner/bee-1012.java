package beginner;

import java.io.IOException;
import java.util.Scanner;

public class Area {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        double a,b,c, aTriangle,aCircle, aTrapezium,aSquare, aRectangle;
        double PI = 3.14159;

        a = sc.nextDouble();
        b = sc.nextDouble();
        c = sc.nextDouble();

        aTriangle = (a * c)/2;
        aCircle = PI*c*c;
        aTrapezium = ((a+b)*c)/2;
        aSquare = b*b;
        aRectangle = a*b;

        System.out.printf("TRIANGULO: %.3f\n", aTriangle);
        System.out.printf("CIRCULO: %.3f\n", aCircle);
        System.out.printf("TRAPEZIO: %.3f\n", aTrapezium);
        System.out.printf("QUADRADO: %.3f\n", aSquare);
        System.out.printf("RETANGULO: %.3f\n", aRectangle);
    }
}
