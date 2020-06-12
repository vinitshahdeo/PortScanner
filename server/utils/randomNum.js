/**
 * 
 * Returns a random number between min (inclusive) and max (exclusive)
 */
function randomNumber(min, max) {
    return Math.floor(
        Math.random() * (max - min) + min
    )
}

module.exports = randomNumber;