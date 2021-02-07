package beginner;
// TODO

import java.io.IOException;
import java.util.Scanner;

public class URI_1984_ThePronalânciaPuzzle {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        String N = String.valueOf(scanner.nextLong());
        StringBuilder sb = new StringBuilder(N);
        String inverse = String.valueOf(sb.reverse());
        System.out.println(inverse);
    }
}