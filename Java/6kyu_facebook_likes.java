class Main {

    class Solution {
        public static String whoLikesIt(String... names) {
            if(names.length == 0){
                return "no one likes this";
            } else if (names.length == 1) {
                return names[0] + " likes this";
            } else if (names.length == 2) {
                return names[0] + " and " + names[1] + " like this";
            } else if (names.length == 3) {
                return names[0] + ", " + names[1] + " and " + names[2] + " like this";
            } else {
                return names[0] + ", " + names[1] + " and " + (names.length - 2) + " others like this";
            }
        }
    }

    public static void main (String[] args) {
        //test
        System.out.println(Solution.whoLikesIt());                                          //"no one likes this"
        System.out.println(Solution.whoLikesIt("Peter"));                           //"Peter likes this"
        System.out.println(Solution.whoLikesIt("Jacob", "Alex"));                   //"Jacob and Alex like this"
        System.out.println(Solution.whoLikesIt("Max", "John", "Mark"));             //"Max, John and Mark like this"
        System.out.println(Solution.whoLikesIt("Alex", "Jacob", "Mark", "Max"));    //"Alex, Jacob and 2 others like this"
    }

}
