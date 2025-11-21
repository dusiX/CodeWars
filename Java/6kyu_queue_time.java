import java.util.Arrays;
import java.util.Collections;

class Main {

    public class Solution {

        public static int solveSuperMarketQueue(int[] customers, int n) {
            int sum = 0;

            if (customers.length == 1){
                return customers[0];
            }

            if(n == 1){
                for (int customer : customers) {
                    sum += customer;
                }
                return sum;
            } else if (n < customers.length){
                int[] summ = new int[n];
                System.arraycopy(customers, 0, summ, 0, n);

                for(int i = n; i < customers.length; i++){
                    Arrays.sort(summ);
                    summ[0] += customers[i];
                }

                Arrays.sort(summ);
                return summ[n-1];
            } else {
                int[] summ = new int[customers.length];
                System.arraycopy(customers, 0, summ, 0, customers.length);
                Arrays.sort(summ);
                return summ[customers.length-1];
            }
        }

    }

    public static void main (String[] args) {
        //test
        System.out.println(Solution.solveSuperMarketQueue(new int[] { 2, 2, 3, 3, 4, 4 }, 10));  //4

        System.out.println(Solution.solveSuperMarketQueue(new int[] { 6, 6, 2, 2, 5, 2, 3, 2, 2, 4, 6, 1, 7 }, 5));  //13

        System.out.println(Solution.solveSuperMarketQueue(new int[] {}, 1));                    //0

        System.out.println(Solution.solveSuperMarketQueue(new int[] { 1, 2, 3, 4, 5 }, 1));     //15
    }

}
