function scrambledPalindromeCheck(str) {
    let count = {};
    let palindrome = 0;

    for (let i = 0; i < str.length; i += 1) {
        count[str[i]] = count[str[i]] || 0;
        count[str[i]] += 1;
    }
    for (let key in count) {
        let splitted = count[key] % 2;
        palindrome += splitted
    }

    return palindrome < 2;
}



console.log(scrambledPalindromeCheck("carrace"));   // true (racecar)
console.log(scrambledPalindromeCheck("bba"));       // true (bab)
console.log(scrambledPalindromeCheck("e"));         // true (e)
console.log(scrambledPalindromeCheck("zzzaaa"));    // false
console.log(scrambledPalindromeCheck("cattaco"));   // true (tacocat)
console.log(scrambledPalindromeCheck("jjqqqjjx"));  // false