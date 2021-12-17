/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    if(s[0] === ")" || s[0] === "]" || s[0] === "}"){
        return false
    }
    else{
        stack.push(s[0])
        for(let i = 1; i < s.length; i++){
            if(s[i] === "(" || s[i] === "{" || s[i] === "["){
                stack.push(s[i])
            }
            else if(s[i] === ")" && stack[stack.length-1] === "(" || s[i] === "}" && stack[stack.length-1] === "{"|| s[i] === "]" && stack[stack.length-1] === "["){
               stack.pop()
            }
            else 
                stack.push(s[i])
            
        }
    }
    
    if(stack.length == 0)
        return true
    else
        return false
    
};
