class Main {

    public static class PangramChecker {
        public boolean check(String sentence){
            long letters = sentence.toLowerCase().chars()
                    .filter(ch -> ch >= 'a' && ch <= 'z')
                    .distinct().count();
            return letters == 26;
        }
    }

    public static void main (String[] args) {
        //test
        String pangram1 = "The quick brown fox jumps over the lazy dog.";
        PangramChecker pc = new PangramChecker();
        System.out.println(pc.check(pangram1)); //true

        String pangram2 = "You shall not pass!";
        PangramChecker pc2 = new PangramChecker();
        System.out.println(pc2.check(pangram2)); //false
    }

}
