class Main {

    public static class Sum
    {
        public int GetSum(int a, int b)
        {
            if(a == b){
                return a;
            }else if(a < b){
                for(int i = a + 1; i <= b; i++) {
                    a += i;
                }
                return a;
            }else if(a > b) {
                for (int i = b + 1; i <= a; i++) {
                    b += i;
                }
                return b;
            }
            return 0;
        }
    }

    public static void main (String[] args) {
        //test
        Sum s = new Sum();

        System.out.println(s.GetSum(0, -1));    //-1
        System.out.println(s.GetSum(0, 1));     //1
        System.out.println(s.GetSum(-20, 5));   //-195

    }

}
