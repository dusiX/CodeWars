class Main {

    class Kata {
        public static String getMiddle(String word) {
            if(word.length() % 2 == 0){
                return String.valueOf(word.charAt((word.length()/2) - 1)) + String.valueOf(word.charAt((word.length()/2)));
            }else{
                return String.valueOf(word.charAt(word.length()/2));
            }
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(Kata.getMiddle("test")); //"es"
        System.out.println(Kata.getMiddle("middle")); //"dd"
        System.out.println(Kata.getMiddle("testing")); //"t"
        System.out.println(Kata.getMiddle("A")); //"A"
    }

}
