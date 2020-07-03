#!/usr/bin/node
// prints C is fun,Python is cool,Javascript is amazing
const num = process.argv[2];
if (num == null) {
     console.log('Missing number of occurrences');
     return;
}

for (i = 0; i < num; i++) {
    if (num > 0) {
	console.log('C is fun')
    } else {
	;
    }
}
