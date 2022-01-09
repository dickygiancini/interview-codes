function reverseDomain(input)
{
    var result = [];
    for(var i = input.length-1; i >= 0;i--)
    {
        result.push(input[i]);
    }

    return result;
}

const parameter1 = ["g", "o", "o", "g", "l", "e", ".", "c", "o", "m"]
const parameter2 = ["g", "o", "o", "g", "l", "e", ".", "c", "o", ".", "i", "d"]
console.log(reverseDomain(parameter1)) // ['m', 'o', 'c', '.','e', 'l', 'g', 'o','o', 'g']
console.log(reverseDomain(parameter2)) // ['d', 'i', '.', 'o','c', '.', 'e', 'l','g', 'o', 'o', 'g']