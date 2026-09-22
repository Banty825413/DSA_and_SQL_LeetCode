class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int carry = 0 ;
        int i = a.length() - 1;
        int j = b.length() -1;

        while (i >= 0 || j >= 0 || carry != 0){
            int temp = carry;
            if (i>= 0 ){
                temp += a.charAt(i) - '0';
                i--;
            }
            if (j >= 0 ){
                temp += b.charAt(j) - '0';
                j--;
            }
            result.append(temp %2);
            carry = temp /2;

        }
        return result.reverse().toString();
    }
}