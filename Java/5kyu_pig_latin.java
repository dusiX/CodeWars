class Main {

    public class PigLatin {
        public static String pigIt(String str) {
            String[] array = str.split(" ");

            int i = 0;

            for (String string : array) {
                if(!(array[i].equals("!") || array[i].equals(",") || array[i].equals(".") || array[i].equals("?"))) {
                    array[i] = new StringBuilder(string).append(array[i].charAt(0)).append("ay").deleteCharAt(0).toString();
                }
                i++;
            }

            return String.join(" ",array);
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(PigLatin.pigIt("Pig latin is cool !")); //"igPay atinlay siay oolcay"
        System.out.println(PigLatin.pigIt("This is my string")); //"hisTay siay ymay tringsay"
    }

}
