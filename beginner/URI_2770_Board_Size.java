package beginner;

import java.io.IOException;
import java.util.Scanner;

public class URI_2770_Board_Size {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            String splitA[] = sc.nextLine().split(" ");
            int a = Integer.parseInt(splitA[0]);
            int b = Integer.parseInt(splitA[1]);
            int times = Integer.parseInt(splitA[2]);

            for (int i = 0; i < times; i++) {
                splitA = sc.nextLine().split(" ");
                int one = Integer.parseInt(splitA[0]);
                int two = Integer.parseInt(splitA[1]);
                boolean flag = false;
                int max = Math.max(a, b);
                int min = Math.min(a, b);

                if (one <= max && two <= max) {
                    flag = true;
                    if (one == max) {
                        if (two > min) {
                            flag = false;
                        }
                    }
                    if (two == max) {
                        if (one > min) {
                            flag = false;
                        }
                    }
                    if (one > min && two > min) {
                        flag = false;
                    }
                } else {
                    flag = false;
                }

                if (flag) {
                    System.out.println("Sim");
                } else {
                    System.out.println("Nao");
                }
            }
        }
    }
}
