const reverse_binary = (number) => {
    const binary = number.toString(2)
    // reverse the binary
    const reversed = binary.split('').reverse().join('')

    // convert back to base 10
    return parseInt(reversed, 2)
}

console.log(reverse_binary(13));
