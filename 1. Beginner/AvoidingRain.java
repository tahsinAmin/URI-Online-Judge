package beginner;
import java.io.IOException;
import java.util.Scanner;

public class AvoidingRain {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int officeNeed = 0, homeNeed = 0, presentHome = 0, presentOffice = 0;

        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String splitA[] = sc.nextLine().split(" ");
            if (splitA[0].equals("chuva")) {
                if (presentHome >0){
                    presentHome--;
                    presentOffice++;
                }else{
                    homeNeed++;
                    presentOffice++;
                }
            }
            if (splitA[1].equals("chuva")) {
                if (presentOffice >0){
                    presentOffice--;
                    presentHome++;
                }else{
                    officeNeed++;
                    presentHome++;
                }
            }
        }
        System.out.printf("%s %s\n", homeNeed, officeNeed);
    }
}