class Main {

    public class FindOutlier{
        static int find(int[] integers){
            int odd = 0, singleodd = 0, singleeven = 0;
            for (int integer : integers) {
                if(integer % 2 == 0) {
                    odd++;
                    singleodd = integer;
                } else {
                    singleeven = integer;
                }
            }
            if (odd == 1){
                return singleodd;
            } else {
                return singleeven;
            }
        }
    }

    public static void main (String[] args) {
        //test
        int[] exampleTest1 = {2,6,8,-10,3};
        int[] exampleTest2 = {206847684,1056521,7,17,1901,21104421,7,1,35521,1,7781};
        int[] exampleTest3 = {Integer.MAX_VALUE, 0, 1};
        System.out.println(FindOutlier.find(exampleTest1)); //3
        System.out.println(FindOutlier.find(exampleTest2)); //0
        System.out.println(FindOutlier.find(exampleTest3)); //0
    }

}
