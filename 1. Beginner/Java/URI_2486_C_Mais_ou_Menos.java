package beginner;
// TODO Change the case values

import java.util.Scanner;

public class URI_2486_C_Mais_ou_Menos {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        while (n != 0) {
            int amount = 0;
            while (n-- > 0) {
                int x = sc.nextInt();
                String s = sc.nextLine().trim();

                switch (s) {
                    case "suco de laranja":
                        amount += 120 * x;
                        break;
                    case "morango fresco":
                        amount += 85 * x;
                        break;
                    case "mamao":
                        amount += 85 * x;
                        break;
                    case "goiaba vermelha":
                        amount += 70 * x;
                        break;
                    case "manga":
                        amount += 56 * x;
                        break;
                    case "laranja":
                        amount += 50 * x;
                        break;
                    case "brocolis":
                        amount += 34 * x;
                        break;
                }
            }
            String t = (amount > 130) ? "Menos " + (amount - 130) :
                    (amount < 110) ? "Mais " + (110 - amount) : "" + amount;
            System.out.println(t + " mg");

            n = sc.nextInt();
        }
    }
}