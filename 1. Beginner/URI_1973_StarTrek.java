package beginner;

import java.io.IOException;
import java.util.Scanner;

// Code that got compiled
public class URI_1973_StarTrek {
    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        int N = leitor.nextInt();
        int[] estrela = new int[N];
        int[] carneiro = new int[N];
        long totalEstrela = 0;
        long totalCarneiro = 0;

        for (int i = 0; i < N; i++) {
            carneiro[i] = leitor.nextInt();
            estrela[i] = 0;
        }

        int j = 0;

        while (true) {
            if (j == 0 && carneiro[j] % 2 == 0) {
                estrela[j] = 1;
                if (carneiro[j] > 0) carneiro[j]--;
                break;
            } else if (j == (N - 1) && carneiro[j] % 2 == 1) {
                estrela[j] = 1;
                if (carneiro[j] > 0) carneiro[j]--;
                break;
            } else if (carneiro[j] % 2 == 1) {
                if (carneiro[j] > 0) carneiro[j]--;
                estrela[j] = 1;
                j++;
            } else if (carneiro[j] % 2 == 0) {
                estrela[j] = 1;
                if (carneiro[j] > 0) carneiro[j]--;
                j--;
            }
        }

        for (int i = 0; i < N; i++) {
            totalCarneiro += carneiro[i];
            totalEstrela += estrela[i];
        }

        System.out.println(totalEstrela + " " + totalCarneiro);
    }
}
//    My Code which didn't
//    public static void main(String[] args) throws IOException {
//        Scanner scanner = new Scanner(System.in);
//
//        int n = scanner.nextInt();
//        int[] leftArray = new int[n];
//        long left = 0, stolen = 0;
//        boolean flag = true;
//
//
//
//        for (int i=0; i<n; i++){
//            leftArray[i] = scanner.nextInt();
//        }
//
//        for (int i=0; i<n; ){
//            if ((i==0 && leftArray[i]%2==0) || (i==n-1 && leftArray[i]%2==1)){
//                leftArray[i] -= (leftArray[i] > 0) ?  1: 0;
//                break;
//            }else if(leftArray[i]%2==1){
//                leftArray[i] -= (leftArray[i] > 0) ?  1: 0;
//                i++;
//            }else if(leftArray[i]%2==0){
//                if (flag==true){
//                    stolen = i+1;
//                    flag= false;
//                }
//                leftArray[i] -= (leftArray[i] > 0) ?  1: 0;
//                i--;
//            }
//        }
//
//        stolen = (flag)? n : stolen;
//
//        for (int j = 0; j< n; j++){
//            left+=leftArray[j];
//        }
//        System.out.printf("%d %d",stolen, left);
//    }
