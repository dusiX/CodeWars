import java.util.ArrayList;

class Main {

    static class Metro {

        public static int countPassengers(ArrayList<int[]> stops) {
            int passengersleft = 0;
            for(int i = 0; i < stops.size(); i++){
                passengersleft += stops.get(i)[0];
                passengersleft -= stops.get(i)[1];
            }
            return passengersleft;
        }
    }

    public static void main (String[] args) {
        //test
        Metro metro = new Metro();

        ArrayList<int[]> list = new ArrayList<int[]>();
        list.add(new int[] {10,0});
        list.add(new int[] {3,5});
        list.add(new int[] {2,5});
        System.out.println(metro.countPassengers(list)); //5

    }

}
