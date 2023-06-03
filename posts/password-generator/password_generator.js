const upperCase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]
const lowerCase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
const digits = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]
const special = [
    '!', '@', '#', '$', '%', 
    '^', '&', '*', '(', ')',
    '<', '>', ',', '.', '?',
    '/', '|', '[', ']', ';',
    ':', '{', '}', '-', '+',
    '`', '~'
]
 
function generateRandomCharacter(
    useUpperCase,
    useLowerCase,
    useDigits,
    useSpecial
) {
    var chars = [];
    if (useUpperCase) { chars = [...chars, ...upperCase]; }
    if (useLowerCase) { chars = [...chars, ...lowerCase]; }
    if (useDigits) { chars = [...chars, ...digits]; }
    if (useSpecial) { chars = [...chars, ...special]; }
    return chars[Math.floor(Math.random() * chars.length)];
}
 
function generateRandomString(length, type) {
    var s = '';
    for (let i = 0; i < length; i++) {
        if (type == 'numeric') {
            var char = generateRandomCharacter(
                false, false, true, false
            );
        }
        if (type == 'alpha') {
            var char = generateRandomCharacter(
                true, true, false, false
            );
        }
        if (type == 'alphanumeric') {
            var char = generateRandomCharacter(
                true, true, true, false
            );
        }
        if (type == 'everything') {
            var char = generateRandomCharacter(
                true, true, true, true
            );
        }
        s = s + char;
    }
    return s;
}
 
function generateAndUpdate() {
    // get value of length input
    var length = document.getElementById('passwordLength').value;
    // get value of type input
    var type;
    document.getElementsByName('passwordType').forEach(
        function(radioElement) { 
            if (radioElement.checked) {
                type = radioElement.id;
            }
        }
    );
    // update password generated field
    var field_contents = generateRandomString(length, type);
    var field = document.getElementById('passwordField');
    field.textContent = field_contents;
}
 
var rangeInput = document.getElementById('passwordLength');
var rangeCurrent = rangeInput.value;
var rangeLabel = document.getElementById('lengthLabel');
rangeLabel.textContent = 'length: ' + rangeCurrent;
rangeInput.addEventListener('input', function(){
    rangeLabel.textContent = 'length: ' + rangeInput.value;
});
