package everyday_one_leco;

public class squareIsWhiteSolution {
    public boolean squareIsWhite(String coordinates) {
        char first = coordinates.charAt(0);
        char second = coordinates.charAt(1);

        boolean flag = true;
        if((first-'0')%2==1){
            flag = (second-'0')%2==1 ? false:true;
        }else{
            flag = (second-'0')%2==1 ? true:false;
        }
        return flag;
    }

    public static void main(String[] args) {
        String coordinates = "c7";
        squareIsWhiteSolution solution = new squareIsWhiteSolution();
        boolean res = solution.squareIsWhite(coordinates);
        System.out.println(res);
    }
}
