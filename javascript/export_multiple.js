const makeFirstCharCapital = (str) => {
    return str[0].toUpperCase() + str.slice(1, str.length);
}

const makeLastCharCapital = (str) => {
    return str.slice(0, str.length-1) + str[str.length-1].toUpperCase();
}

const makeFullStringCapital = (str) => {
    return str.toUpperCase();
}

export const PI = 3.1415;
export const e = 2.73;

export {makeFirstCharCapital, makeLastCharCapital}