let a = 10;
let b = 5;

console.log("Addition: " + (a + b));
console.log("Substraction " + (a - b));
console.log("Multiplication: " + (a * b));
console.log("Division: " + (a / b));
console.log("Modulus: " + (a % b));
console.log("Exponentiation: " + (a ** b));

let age = 20;
let isRegistered = true;

if (age => 18 && isRegistered) {
    console.log("VOTE");
} else {
    console.log("Do not vote");
}

let num1 = 15;
let num2 = 2;

if (num1 > num2) {
    console.log("Num1 is greater that num2");
} else if (num1 < num2) {
    console.log("Num2 is greater that num1");
} else {
    console.log("both nums are equal");
}

let MEGAULTRADUPERNUMBER = -12;

if (MEGAULTRADUPERNUMBER > 0) {
    console.log("MEGAULTRADUPERNUMBER is positive");
} else if (MEGAULTRADUPERNUMBER < 0) {
    console.log("MEGAULTRADUPERNUMBER is negative");
} else {
    console.log("MEGAULTRADUPERNUMBER is zero");
}

let day = "Friday";

switch (day){
    case "Monday":
        console.log("Start of the week!");
        break;
    case "Friday":
        console.log("Weekend is near");
        break;
    case "Sunday":
        console.log("REST DAYYYY");
        break;
    default:
        console.log("regular day");
        break;
}

let c = 17;
let res = (c % 2 ===0)?"Even":"Odd";
console.log("Number is: ", res);