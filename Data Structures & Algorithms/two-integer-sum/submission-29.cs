public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> map = new Dictionary <int,int> ();
        for( int i = 0; i < nums.Length; i++  ) {
            var complement = target - nums[i];
            if(map.ContainsKey(complement)) {
                return new int [] {map[complement], i};
            }
            map[nums[i]] = i;

        }
        return null;
    }
    

}


/*/
hey so this is my approach

    first i think i would go about making a hashmap that has its complement to it and if it finds it then it would go about doing it ifykwhatimsaying
/*/