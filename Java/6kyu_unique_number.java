import java.util.Arrays;

class Main {

    public class Kata {
        public static double findUniq(double arr[]) {
            double num = 0;
            int count = 0;

            for (int i = 0; i < arr.length; i++){
                for (int j = 0; j < arr.length; j++){
                    if (arr[i] == arr[j] && i != j){
                        count++;
                        break;
                    }
                }
                if (count == 0){
                    num = arr[i];
                    return num;
                }
                count = 0;
            }

            return num;
        }
    }

    public static void main (String[] args) {
        //test
        double precision = 0.0000000000001;
        System.out.println(Kata.findUniq(new double[]{0, 1, 0}));             //1.0
        System.out.println(Kata.findUniq(new double[]{1, 1, 1, 2, 1, 1, 3, 3}));    //2.0
    }

}
