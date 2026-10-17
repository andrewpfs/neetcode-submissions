public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary <char,int> letterCounts = new Dictionary<char,int> ();

        foreach (char sChar in s) {
            if (letterCounts.ContainsKey(sChar)) {
                letterCounts[sChar] ++;
            }
            else {
                letterCounts[sChar] = 1;
            }
        }
        foreach(char tChar in t) {
            if(letterCounts.ContainsKey(tChar)){
                letterCounts[tChar] --;
            }
            else {
                letterCounts[tChar] = 1;
            }
        }
        foreach (var res in letterCounts ){
            if(res.Value != 0 ) {
                return false;
            }
        }
        return true;
    }
}
