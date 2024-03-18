impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let n = s.len();
        let mid = s.len()/2;
        for i in (0..mid){
            let temp = s[i];
            s[i] = s[n - 1 - i]; 
            s[n - 1 - i] = temp; 
        }
    }
}
