class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> tri = new ArrayList<>();
        List<Integer> first = new ArrayList<>();
        first.add(1);
        tri.add(first);

        for (int i = 1; i < numRows ; i++){

            List<Integer> prev = tri.get(i-1);
            
            List<Integer> temp = new ArrayList<>();
            temp.add(0);
            temp.addAll(prev);
            temp.add(0);
            List<Integer> new_row  = new ArrayList<>();
            for (int j = 0 ; j <= prev.size()  ; j++  ){
                new_row.add(temp.get(j)+temp.get(j+1));
            }
            tri.add(new_row);
        }
        return tri;

        
    }
}