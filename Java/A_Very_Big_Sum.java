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

 /* File Name : A_Very_Big_Sum.java
*  Date Created : 20/8/2019
 */
public class A_Very_Big_Sum {

    // Complete the aVeryBigSum function below.
    static long aVeryBigSum(long[] ar) {
        long total = 0;

        for (int i = 0; i < ar.length; i++) {
            total += ar[i];
        }

        return total;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        long[] ar = new long[arCount];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < arCount; i++) {
            long arItem = Long.parseLong(arItems[i]);
            ar[i] = arItem;
        }

        long result = aVeryBigSum(ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
