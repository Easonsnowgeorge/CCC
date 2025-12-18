import java.io.*;
import java.util.*;

public class CCC00S2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Double> flows = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            double flow = Double.parseDouble(br.readLine());
            flows.add(flow);
        }
        while (true) {
            int decision = Integer.parseInt(br.readLine());
            if (decision == 99) {
                int number = Integer.parseInt(br.readLine());
                int percent = Integer.parseInt(br.readLine());
                double flow = flows.get(number - 1);
                flows.set(number - 1, (double)((flow * percent) / 100));
                flows.add(number, (double)(flow * (100 - percent) / 100));
            }
            else if (decision == 88) {
                int number = Integer.parseInt(br.readLine());
                flows.set(number - 1, flows.get(number - 1) + flows.get(number)); 
                flows.remove(number);
            }
            else if (decision == 77) break;
        }
        for (double i : flows) {
            System.out.print((int)Math.floor(i) + " ");
        }
    }
}