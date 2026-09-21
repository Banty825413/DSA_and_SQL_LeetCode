class Solution {
    public List<Integer> getRow(int rowIndex) {
        
      
        ArrayList <Integer> arr = new ArrayList<>();
        arr.add(1);
          if (rowIndex == 0) {
            return arr;
        }
        for (int i = 0 ; i <rowIndex ; i++){
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(0);
            temp.addAll(arr);
            temp.add(0);
            ArrayList<Integer> result = new ArrayList<>();
            for (int j= 0 ; j< arr.size()+1 ; j++){
                result.add(temp.get(j)+ temp.get(j+1));
            }
            arr = result;
        }
        return arr;
    }
}