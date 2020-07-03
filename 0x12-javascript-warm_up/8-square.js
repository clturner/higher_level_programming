#!/usr/bin/node
// print a square
const arg = process.argv[2];
const arg2 = process.argv[2];

if (isNaN(arg2) == true || arg == null) {
    console.log('Missing size');
} else {
    for (i = 0; i < arg; i++) {
	for (j = 0; j < arg; j++) {
            process.stdout.write('X');
        }
	process.stdout.write('\n');
    }
}
