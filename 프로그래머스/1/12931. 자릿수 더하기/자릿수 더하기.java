import java.util.*;

public class Solution {
    public int solution(int n) {
        int sum = 0;
        String answer = Integer.toString(n);
        for (int i = 0; i < answer.length() ; i++){
            int b = n % 10;
            n = n / 10;
            sum += b;
        }
        

       
        return sum;
    }
}