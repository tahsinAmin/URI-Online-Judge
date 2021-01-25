package IMight;

// TODO https://www.urionlinejudge.com.br/judge/en/problems/view/2632
//  URI_2632_Magic_and_Sword

import java.util.Scanner;

public class URI_2632_Magic_and_Sword {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[][] sDR = {
                {200, 20, 30, 50},
                {300, 10, 25, 40},
                {400, 25, 55, 70},
                {100, 18, 38, 60},
        };

        int rWidth, rHeight,rX, rY;

        String spellIdentifier; int level, sX,sY;

//        for (int i = 0; i < sDR.length; i++) {
//            for (int j = 0; j < sDR[i].length; j++) {
//                System.out.print(sDR[i][j] + " ");
//            }
//            System.out.println();
//        }

        int testCases = sc.nextInt();

        while(testCases-- > 0){
            rWidth = sc.nextInt();
            rHeight = sc.nextInt();
            rX = sc.nextInt();
            rY = sc.nextInt();

            spellIdentifier = sc.next();
            level = sc.nextInt();
            sX = sc.nextInt();
            sY = sc.nextInt();

            System.out.printf("%d %d %d %d\n",rWidth, rHeight, rX, rY);
            System.out.printf("%s %d %d %d\n", spellIdentifier, level, sX, sY);

            int lowerRightX = rX + rWidth;
            int lowerRightY = rY;

            int upperRightX = lowerRightX;
            int upperRightY = rY + rHeight;

//            int d1 = Math.sqrt(Math.pow((lowerRightX-xI),2.0) + Math.pow((yF-yI),2.0)) + vI*1.50;
        }
    }
}