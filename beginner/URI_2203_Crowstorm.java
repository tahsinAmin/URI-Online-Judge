package beginner;

// TODO https://www.urionlinejudge.com.br/judge/en/problems/view/2203

import java.util.Scanner;

public class URI_2203_Crowstorm {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int xF,yF,xI,yI,vI;
        double radiusCast, radiusCrows, d1, d2;

        while(scanner.hasNext()){
            xF = scanner.nextInt();
            yF = scanner.nextInt();

            xI = scanner.nextInt();
            yI = scanner.nextInt();

            vI = scanner.nextInt();

            radiusCast = scanner.nextInt();
            radiusCrows = scanner.nextInt();

            d1 = Math.sqrt(Math.pow((xF-xI),2.0) + Math.pow((yF-yI),2.0)) + vI*1.50;
            d2 = radiusCast + radiusCrows;

            String s = (d1 > d2) ? "N" : "Y";
            System.out.println(s);
        }
    }
}