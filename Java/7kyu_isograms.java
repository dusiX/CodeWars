class Main {

    public class isogram {
        public static boolean  isIsogram(String str) {
            String x = str.toLowerCase();
            for (int i = 0; i < str.length(); i++){
                for (int j = i + 1; j < str.length(); j++){
                    if(x.charAt(i) == x.charAt(j)){
                        return false;
                    }
                }
            }
            return true;
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(isogram.isIsogram("Dermatoglyphics"));       //true
        System.out.println(isogram.isIsogram("isogram"));               //true
        System.out.println(isogram.isIsogram("moose"));                 //false
        System.out.println(isogram.isIsogram("isIsogram"));             //false
        System.out.println(isogram.isIsogram("aba"));                   //false
        System.out.println(isogram.isIsogram("moOse"));                 //false
        System.out.println(isogram.isIsogram("thumbscrewjapingly"));    //true
        System.out.println(isogram.isIsogram(""));                      //true
    }

}
