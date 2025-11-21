// Programme finds a number in provided array which occurs an odd number of times

class Main {

    public class FindOdd {
        public static int findIt(int[] a) {
            int odd = 0, count = 0;
            for(int i = 0; i < a.length; i++){
                for(int j = 0; j < a.length; j++){
                    if(a[i] == a[j]){
                        count++;
                    }
                }
                if(count % 2 == 1){
                    odd = a[i];
                }
                count = 0;
            }
            return odd;
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(FindOdd.findIt(new int[]{20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5}));         //5
        System.out.println(FindOdd.findIt(new int[]{1,1,2,-2,5,2,4,4,-1,-2,5}));                        //-1
        System.out.println(FindOdd.findIt(new int[]{20,1,1,2,2,3,3,5,5,4,20,4,5}));                     //5
        System.out.println(FindOdd.findIt(new int[]{10}));                                              //10
        System.out.println(FindOdd.findIt(new int[]{1,1,1,1,1,1,10,1,1,1,1}));                          //10
        System.out.println(FindOdd.findIt(new int[]{5,4,3,2,1,5,4,3,2,10,10}));                         //1
    }

}
