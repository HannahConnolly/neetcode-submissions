class Solution {

    public boolean isValid(String s) {
    
        Stack<Character> bracketStack = new Stack<Character>();
        Hashtable<Character, Character> bracketPairs = new Hashtable<Character, Character>();
       
        bracketPairs.put('}', '{');
        bracketPairs.put(')', '(');
        bracketPairs.put(']', '[');
    
        for(int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            System.out.println(current);
            if(current == '{' || current == '(' || current == '[') {
                bracketStack.add(current);
            }
            else {
                System.out.println(bracketPairs.get(current));
                if(bracketStack.size() == 0 || bracketStack.pop() != bracketPairs.get(current)) {
                    return false;
                }
            }
        }
        return bracketStack.size() == 0 ;
    }
}
