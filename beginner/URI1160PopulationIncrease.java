package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI1160PopulationIncrease {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        while(n-- > 0){
            int cityA = sc.nextInt();
            int cityB = sc.nextInt();
            double growthA = sc.nextDouble();
            double growthB = sc.nextDouble();
            
            int count= 0;

            while(cityA<= cityB){
                cityA = (int) (cityA * (growthA/100.0) + cityA);
                cityB = (int) (cityB * (growthB/100.0) + cityB);
                if (++count > 100) {
                    break;
                }
            }

            if (count > 100) {
                System.out.println("Mais de 1 seculo.");
            } else {
                System.out.println(count + " anos.");
            }
        }
    }
}