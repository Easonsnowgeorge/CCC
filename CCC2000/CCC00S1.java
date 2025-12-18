import java.util.Scanner;

public class CCC00S1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int quarters = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int plays = 0;

        while (quarters > 0) {
            // Machine A
            quarters--;
            plays++;
            a++;
            if (a == 35) {
                quarters += 30;
                a = 0;
            }
            if (quarters == 0)
                break;

            // Machine B
            quarters--;
            plays++;
            b++;
            if (b == 100) {
                quarters += 60;
                b = 0;
            }
            if (quarters == 0)
                break;

            // Machine C
            quarters--;
            plays++;
            c++;
            if (c == 10) {
                quarters += 9;
                c = 0;
            }
        }

        System.out.println("Martha plays " + plays + " times before going broke.");
    }
}