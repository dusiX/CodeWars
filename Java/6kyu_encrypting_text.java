import java.util.Arrays;

class Main {

    public class Kata {

        public static String encrypt(final String text, final int n) {
            String str = "", textcopy = text;

            for(int i = 0; i < n; i++){
                for(int j = 1; j < textcopy.length(); j++){
                    str = str.concat(String.valueOf(textcopy.charAt(j)));
                    j++;
                }
                for(int j = 0; j < textcopy.length(); j++){
                    str = str.concat(String.valueOf(textcopy.charAt(j)));
                    j++;
                }
                textcopy = str;
                str = "";
            }

            return textcopy;
        }

        public static String decrypt(final String encryptedText, final int n) {
            if(encryptedText == null){
                return encryptedText;
            }

            char[] text = encryptedText.toCharArray();
            char[] finalstring = encryptedText.toCharArray();
            int k = 0;

            for(int i = 0; i < n; i++){
                for(int j = 1; j < text.length; j++){
                    finalstring[j++] = text[k++];
                }
                for(int j = 0; j < text.length; j++){
                    finalstring[j++] = text[k++];
                }
                System.arraycopy(finalstring, 0, text, 0, text.length);
                k = 0;
            }

            return String.valueOf(finalstring);
        }



    }

    public static void main (String[] args) {
        //test
        System.out.println(Kata.encrypt("This is a test!", 0));                 //"This is a test!"
        System.out.println(Kata.encrypt("This is a test!", 1));                 //"hsi  etTi sats!"
        System.out.println(Kata.encrypt("This is a test!", 2));                 //"s eT ashi tist!"
        System.out.println(Kata.encrypt("This is a test!", 3));                 //" Tah itse sits!"
        System.out.println(Kata.encrypt("This is a test!", 4));                 //"This is a test!"
        System.out.println(Kata.encrypt("This is a test!", -1));                //"This is a test!"
        System.out.println(Kata.encrypt("This kata is very interesting!", 1));  //"hskt svr neetn!Ti aai eyitrsig"


        System.out.println(Kata.decrypt("This is a test!", 0));                 //"This is a test!"
        System.out.println(Kata.decrypt("hsi  etTi sats!", 1));                 //"This is a test!"
        System.out.println(Kata.decrypt("s eT ashi tist!", 2));                 //"This is a test!"
        System.out.println(Kata.decrypt(" Tah itse sits!", 3));                 //"This is a test!"
        System.out.println(Kata.decrypt("This is a test!", 4));                 //"This is a test!"
        System.out.println(Kata.decrypt("This is a test!", -1));                //"This is a test!"
        System.out.println(Kata.decrypt("hskt svr neetn!Ti aai eyitrsig", 1));  //"This kata is very interesting!"


        System.out.println(Kata.encrypt("", 0));    //""
        System.out.println(Kata.decrypt("", 0));    //""
        System.out.println(Kata.encrypt(null, 0));  //null
        System.out.println(Kata.decrypt(null, 0));  //null
    }

}
