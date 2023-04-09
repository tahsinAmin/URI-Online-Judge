package beginner;
// TODO

import java.io.IOException;
import java.util.Scanner;

//TODO https://www.urionlinejudge.com.br/judge/en/problems/view/1985


public class URI_1985_MacPronalts {
    public static void main(String[] args) throws IOException {

        Scanner scanner = new Scanner(System.in);
        int p = scanner.nextInt();
        double total = 0;
        int q, c;
        for (int i = 0; i < p; i++) {
            c = scanner.nextInt();
            q = scanner.nextInt();
            switch (c) {
                case 1001: total += q * 1.50; break;
                case 1002: total += q * 2.50; break;
                case 1003: total += q * 3.50; break;
                case 1004: total += q * 4.50; break;
                case 1005: total += q * 5.50; break;
            }
        }
        System.out.println(String.format("%.2f", total));
//        Map<Integer,Integer> m = new HashMap<>(){{
//            put(1001, 150); put(1002, 250); put(1003, 350); put(1004, 450); put(1005, 550);
//        }};
//
//        int sum=0,n = scanner.nextInt();
//
//        while(n-- > 0){
//            int key = scanner.nextInt();
//            int quantity = scanner.nextInt();
//            sum+= (m.get(key)*quantity);
//        }
//        System.out.println(String.format("%.2f", sum/100.00));
    }
}