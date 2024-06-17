export function duplicateEncode(word: string): string {
    let result: string = ''
    word.toLowerCase().split('').forEach((l: string) => {
        let count: number = 0
        for (let i = 0; i < word.length; i++) {
            word[i] === l ? count++ : ''
        }
        count <= 1 ? result += '(' : result += ')'
    })
    return result
}

// Expected output

// "din"      =>  "((("
// "recede"   =>  "()()()"
// "Success"  =>  ")())())"
// "(( @"     =>  "))((" 

console.log(duplicateEncode("din"))
console.log(duplicateEncode("recede"))
console.log(duplicateEncode("Success"))
console.log(duplicateEncode("(( @"))
