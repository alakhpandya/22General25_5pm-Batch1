let quoteArray = [
    {
        quote: "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live",
        author: "John Woods"
    }, 
    {
        quote:"Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        author:"Martin Fowler"
    },
    {
        quote : "Programmers seem to be changing the world. It would be a relief, for them and for all of us, if they knew something about it.",
        author : "Ellen Ullman"
    },
    {
        quote : "It’s not a bug; it’s an undocumented feature.",
        author : "Anonymous"
    },
    {
        quote : "Learning the art of programming, like most other disciplines, consists of first learning the rules and then learning when to break them.",
        author : "Joshua Bloch" 
    },
    {
        quote : "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        author : "Martin Fowler"
    },
    {
        quote: "Every programmer is an author",
        author:"Sercan Leylek"
    },
    {
        quote:"Everyone should learn how to code,it teaches you how to think.",
        author:"Steve Jobs"
    },
    {
        quote:"Progress is possible only if we train ourselves to think about programs without thinking of them as pieces of executable code.",
        author:"Edsger W. Dijkstra"
    },
    {
        quote:"A language that doesn't affect the way you think about programming is not worth knowing.",
        author:"Alan J. Perlis"
    }
];
let quote = document.querySelector('.para');
let author = document.querySelector('.author');
let btn = document.querySelector('.btn1');
let index;

btn.addEventListener('click', () => {
    index = Math.floor(Math.random() * 10);    
    quote.innerText = quoteArray[index]["quote"];
    author.innerText = quoteArray[index]["author"];
})

// console.log(index);
/*
Least possible no: 0 * 10 = 0.000               = 0
Largest possible no: 0.99999 * 10 = 9.9999999   = 9
*/