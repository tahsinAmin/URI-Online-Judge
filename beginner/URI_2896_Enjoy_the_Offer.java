package beginner;

import java.util.Scanner;

public class URI_2896_Enjoy_the_Offer {

        public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                int t = scanner.nextInt();
                scanner.nextLine();
                
                for (int i = 0; i < t; i++) {
                        String s = scanner.nextLine();
                        String splitA[] = s.split(" ");
                        int k = Integer.parseInt(splitA[0]);
                        int n = Integer.parseInt(splitA[1]);

                        if (k == n) {
                                System.out.println(1);
                        } else if (k > n) {
                                System.out.println((k / n) + (k % n));
                        }else{
                                System.out.println(k);
                        }

                }

        }
}
