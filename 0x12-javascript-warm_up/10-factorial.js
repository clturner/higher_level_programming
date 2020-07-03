#!/usr/bin/node
// script that computes and prints a factorial
function factorial (a) {
    if (a == 0) {
        return 1;
    }
    for(i = a; --i; ) {
        a = a*i;
    }
    return a;
}

const answer = factorial(process.argv[2]);
console.log(answer);
