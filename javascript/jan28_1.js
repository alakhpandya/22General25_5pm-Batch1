// Write a function that takes an integer as argument & returns whether its a Prime number or not. Write a main program that takes an integer from user and prints if it is Prime or not using that function.

/*
function primeCheck(n){     // n = 9
    flag = 1;
    for(let i=2; i<n; i++){
        if(n % i == 0){
            console.log("Not Prime.");
            flag = 0;
            break;
            // return false;
        }
    }
    // return true;
    if (flag == 1){
        console.log("Prime.");
    }
}

a = Number(prompt("a: "));
b = Number(prompt("b: "));
for(let i = a; i <= b; i++){
    primeCheck(i);
}
// if (primeCheck(a)){
//     console.log("Prime");
// }
// else{
//     console.log("Not Prime.");
// }
*/
/*
Ask two numbers from user & print all the prime numbers between them.
*/
/*
function primeCheck(n){     // n = 9
    if (n == 1){
        return false;
    }
    for(let i=2; i<n; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

a = Number(prompt("a: "));
b = Number(prompt("b: "));
for(let i = a; i <= b; i++){    // a = 5, b = 10
    if (primeCheck(i)){
        console.log(i);
    }
}
*/

// Iterating over an array using loops:
// var myArray = [12, 19, 81, 0, -21, -34, 19];

/*
for(let i = 0; i < myArray.length; i++){
    console.log(myArray[i]);
}
*/
/*
let i = 0;
while (i < myArray.length){
    console.log(myArray[i] + 10);
    i++;
}
*/
/*
let i = 0;
do{
    console.log(myArray[i] * 10);
    i++;
}while(i < myArray.length);
*/

// counting no of digits
/*
n = Number(prompt("n:"));
digit = 0;
while (n > 0){
    n = Math.floor(n / 10);
    digit++;
}
console.log(digit);
*/

// Arrays
/*
let myArray = [45, 76.87, -89.5, "Ahmedabad", 0, 34, "Delhi", 76, 25];
let fruits = ["apple", "banana", "kiwi", "mango", "grapes", "orange"];
console.log(myArray[3]);
console.log(fruits[3]);
fruits[2] = "strawberry";
console.log(fruits);
*/

// Nested arrays:
// let myMatrix = [[3,5,-8], [24, 55, 0], [12,13,14]]
/*
let myArray = [
    [3, 5, -8],
    ["pavbhaji", "jain khichdi"],
    [24, 55, 0],
    [12, 13, 14]
]

console.log(myArray[0][2]);
console.log(myArray[2][2]);
*/

/*
// push
let myArray = [45, 76.87, -89.5, "Ahmedabad", 0, 34, "Delhi", 76, 25];
myArray.push(1000);
console.log(myArray);

// pop
let a = myArray.pop();
let b = myArray.pop();
console.log(myArray);

// shift
myArray.shift();
console.log(myArray);

// unshift
myArray.unshift(5000);
console.log(myArray);
*/

// User defined array
/*
let customArray = [];
let n = Number(prompt("Number of elements:"));
let e;
for(let i = 0; i < n; i++){
    e = prompt("Element:");
    customArray.push(e);
}
console.log(customArray);
*/
// Next Session: Objects