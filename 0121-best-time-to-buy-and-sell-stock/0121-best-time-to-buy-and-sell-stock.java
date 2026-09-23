class Solution {
    public int maxProfit(int[] prices) {
        int min_price = Integer.MAX_VALUE; 
        int profit = 0;
        for (int price : prices){
            if(min_price > price) {
                min_price = price;
            }
            else if (price - min_price > profit){
                profit = price - min_price;
            }
        }
        return profit;
    }
    
}