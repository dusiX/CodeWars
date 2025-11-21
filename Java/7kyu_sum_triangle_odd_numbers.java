class Main {

    class RowSumOddNumbers {
        public static int rowSumOddNumbers(int n) {
            int sum = 0, j = 1;

            for(int i = 0; i < n; i++) {
                sum += n * (n - 1) + j;
                j += 2;
            }

            return sum;
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(RowSumOddNumbers.rowSumOddNumbers(1));   //1
        System.out.println(RowSumOddNumbers.rowSumOddNumbers(42));  //74088

    }

}
