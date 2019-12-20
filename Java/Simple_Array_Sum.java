/*
*   .-"-.
*  /|6 6|\
* {/(_0_)\}
*  _/ ^ \_
* (/ /^\ \)-'
*  ""' '""     하늘
 */

import java.io.*;
import java.util.*;

/* written by
 *  @author Wolverine 왕경민
 */

 /* File Name : Simple_Array_Sum.java
*  Date Created : 20/8/2019
 */
public class Simple_Array_Sum {

    /*
     * Complete the simpleArraySum function below.
     */
    static int simpleArraySum(int[] ar) {
        int total = 0;
        for (int i = 0; i < ar.length; i++) {
            total += ar[i];
        }

        return total;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arCount = Integer.parseInt(scanner.nextLine().trim());

        int[] ar = new int[arCount];

        String[] arItems = scanner.nextLine().split(" ");

        for (int arItr = 0; arItr < arCount; arItr++) {
            int arItem = Integer.parseInt(arItems[arItr].trim());
            ar[arItr] = arItem;
        }

        int result = simpleArraySum(ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
