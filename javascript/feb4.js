// Objects = dictionaries in Python
/*
let result = {
    "Maths": 85,
    'English': 87,
    Physics: 89
};

console.log(result);
// console.log(result[0]);

// Two ways to access:
console.log(result.Physics);
console.log(result["Maths"]);

let bollywoodHero = {
    hat : "Pink",
    "T-shirt" : "Green",
    trousers : "Purple",
    '2shoes' : "White"
};
console.log(bollywoodHero.hat);
console.log(bollywoodHero["trousers"]);
console.log(bollywoodHero['T-shirt']);
*/
// Nesting of objects
/*
let myHome = {
    outside : "Garden",
    inside : {
        "drawing room": ["TV", "Sofa"],
        "kitchen": ["wife", "mom", "weapons"],
        "my room": {
            mirror: "huge",
            wardrobe : "messy",
            bed : "wooden",
            locker : {
                "outer part" : "Photo Albums",
                "inner locker" : ["gold", "cash"]
            }
        }
    }
}

console.log(myHome.inside["kitchen"][2]);
*/

// Class work
/*
let myCollection = [
    {
        "artist":"2 unlimited",
        "title":"no limit",
        "release_year":1991,
        "formats":[
            "cassate",
            "cd",
            "mp3",
            "youtube"
        ],
        "genre":"rap"
    },
    {
        "artist":"Kungs",
        "title":"this girl",
        "release_year":2016,
        "formats":[
            "mp3",
            "youtube"
        ],
        "genre":"remix"
    }
]

// delete myCollection[1]["formats"][1]
// console.log(myCollection);
*/
// Upcoming topics to learn:
// deleting a property

let bollywoodHero = {
    hat : "Pink",
    "T-shirt" : "Green",
    trousers : "Purple",
    '2shoes' : "White",
    Tie : "red",
    trousers : "Pink"
};

// delete bollywoodHero["Tie"]
// console.log(bollywoodHero);

// hasOwnProperty method
// console.log(bollywoodHero.hasOwnProperty('hat'));
// console.log(bollywoodHero.hasOwnProperty('tail'));

// HW:

function propertyChecker(obj, property){
    // Your code goes here
    if (obj.hasOwnProperty(property)){
        return obj[property];
    }
    else{
        return "Sorry, this property does not exist in the object."
    }
}

// test case-1:

console.log(propertyChecker(bollywoodHero, 'hat'));
// output:
// Pink

// test case-2:

console.log(propertyChecker(bollywoodHero, 'tail'));
// output:
// Sorry, this property does not exist in the object.


// Next Class: Objects as lookup table
