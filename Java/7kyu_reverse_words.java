import java.util.ArrayList;
import java.util.Arrays;

class Main {

    public class Kata
    {
        public static String reverseWords(final String original)
        {
            String[] array = original.split(" ");

            if(array.length == 0)
                return original;


            int i = 0;
            for(String string : array){
                array[i] = new StringBuilder(string).reverse().toString();
                i++;
            }

            return String.join(" ",array);
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(Kata.reverseWords("The quick brown fox jumps over the lazy dog."));  //"ehT kciuq nworb xof spmuj revo eht yzal .god"
        System.out.println(Kata.reverseWords("apple"));                                         //"elppa"
        System.out.println(Kata.reverseWords("a b c d"));                                       //"d c b a"
        System.out.println(Kata.reverseWords("double  spaced  words"));                         //"elbuod  decaps  sdrow"
        System.out.println(Kata.reverseWords("     "));

    }

}
