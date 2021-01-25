package beginner;

import java.util.Scanner;

public class URI_2879_Unraveling_Monty_Hall {

        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                int i = sc.nextInt();
                if (i >= 1 && i <= Math.pow(10, 4)) {

                        
                        int count = 0;

                        for (int j = 0; j < i; j++) {
                                if (1 != sc.nextInt()) {
                                        count++;
                                }
                        }
                        System.out.println(count);
                }
        }

}
