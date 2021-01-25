package beginner;

import java.util.Scanner;

public class URI_2686_The_Change_Continues {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double deg, totalSeconds;
        int hours, minutes, seconds;
        String msg, str;

        while(scanner.hasNext()){
            deg = scanner.nextDouble();
            totalSeconds = deg / 360.0 * 86400 + 21600; // add 360 cos adding 6 hours for printing
            hours = (int) ((totalSeconds / 3600) % 24);
            minutes = (int) (((totalSeconds - (hours * 3600))/60)%60);
            seconds = (int) ((totalSeconds - (hours * 3600))%60);

//            System.out.printf("%d hours %d minutes %d seconds\n", hours, minutes, seconds);
//        System.out.println(hours);
            if (hours >= 0 && hours < 6) {
                msg = "De Madrugada!!";
            } else if (hours >= 6 && hours < 12) {
                msg = "Bom Dia!!";
            } else if (hours >= 12 && hours < 18) {
                msg = "Boa Tarde!!";
            } else {
                msg = "Boa Noite!!";
            }
            str = String.format("%02d:%02d:%02d", hours, minutes, seconds);
            System.out.println(msg + "\n" + str);
        }
    }
}