// Problem #2

// Write a function that checks if a given word is a palindrome. Character case should be ignored.

// Solution2 ->


function isPalindrome(word) {
  word = word.toLowerCase();
  for (var i = 0, j = word.length-1; i < j; i++, j--) {
    if (word[i] !== word[j]) {
      return false;
    }
    return true;
  }
}

console.log(isPalindrome("level"));
console.log(isPalindrome("apple"));
console.log(isPalindrome("tenent"));
