function quarantineZeros(array) {
    for (let i = 0; i < array.length; i += 1){
        if (array[i] === 0) {
            array.push(array.splice(array.indexOf(array[i]), 1)[0]);
        }
    }
    return array
}




console.log(quarantineZeros([0, 1, 0, 3, 12]))             // [1,3,12,0,0]
console.log(quarantineZeros([1, 3, 10, 2]))                // [1,3,10,2]
console.log(quarantineZeros([4, 1, 2, 0, 0, 1, 2, 1, 0]))  // [4,1,2,1,2,1,0,0,0]
console.log(quarantineZeros([6, 1, 2, 3, 5, 1, 0]))        // [6,1,2,3,5,1,0]
console.log(quarantineZeros([0, 6, 1, 2, 3, 5, 1, 0]))     // [6,1,2,3,5,1,0,0]
console.log(quarantineZeros([12, 2, 0, 0, 2, 1]))         // [12,2,2,1,0,0]