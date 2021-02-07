package beginner;

import java.util.Scanner;

public class URI_2930_Final_Thesis_of_Christmas_Depression {

        public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                String splitA[] = sc.nextLine().split(" ");
                int e = Integer.parseInt(splitA[0]);
                int d = Integer.parseInt(splitA[1]);

                while (e > 0 && e < 25 && d > 0) {
                        if (e > d) {
                                System.out.println("Eu odeio a professora!");
                                break;
                        } else if (d - e >= 3) {
                                System.out.println("Muito bem! Apresenta antes do Natal!");
                                break;
                        }
                        System.out.println("Parece o trabalho do meu filho!");
                        if (e + 2 >= 24) {
                                System.out.println("Fail! Entao eh nataaaaal!");
                                break;
                        } else {
                                System.out.println("TCC Apresentado!");
                                break;
                        }
                }
        }
}
