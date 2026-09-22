class Solution {
    public void reverseString(char[] s) {
        int last= s.length -1;
        int first = 0;

        while (first < last ){
            char temp ;
            temp= s[first];
            s[first] = s[last];
            s[last] = temp;
            first++;
            last--;
            
        }
    }
}