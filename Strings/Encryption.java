package Strings;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Encryption {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {

        String s;
        char [] cArr;
        int n = Integer.parseInt(in.readLine()),length, half;

        while(n-- >0){
            cArr = in.readLine().toCharArray();
            for (int j =0; j< cArr.length;j++){
                if (Character.isLetter(cArr[j])){
                    cArr[j] = (char)((int)cArr[j] + 3);
                }
            }
            length = cArr.length;
            half = cArr.length/2;

            for (int j =0; j< half;j++){
                char temp = cArr[j];
                cArr[j] = cArr[length -1 - j];
                cArr[length -1 - j] = temp;
            }

            for (int j =half; j< length;j++){
                cArr[j] = (char)((int)cArr[j] - 1);
            }

            for (char c : cArr){
                out.print(c);
            }
            out.println();
        }
        out.close();
    }
}