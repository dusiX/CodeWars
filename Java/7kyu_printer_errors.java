class Main {

    public class Printer {

        public static String printerError(String s) {
            int count = 0;
            for(int i = 0; i < s.length(); i++) {
                if (s.charAt(i) < 'a' || s.charAt(i) > 'm'){
                    count++;
                }
            }
            String errors = count + "/" + s.length();
            return errors;
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println("printerError Fixed Tests");
        String s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
        System.out.println(Printer.printerError(s)); //"3/56"
    }

}
