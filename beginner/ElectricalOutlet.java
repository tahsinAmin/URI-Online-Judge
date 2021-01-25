package beginner;

import java.util.Scanner;

public class ElectricalOutlet{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

            String[] splitA = sc.nextLine().split(" ");

        System.out.println((
                Integer.parseInt(splitA[0]) +
                        Integer.parseInt(splitA[1])+
                        Integer.parseInt(splitA[2])+
                        Integer.parseInt(splitA[3])) - 3
        );
    }
}