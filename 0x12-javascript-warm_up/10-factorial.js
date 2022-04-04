#!/usr/bin/node
let n = process.argv[2];
let r = 1;
if (isNaN(n)) {
  console.log('1');
  process.exit(1);
}
n = Number(n);
while (n > 0) r *= n--;
console.log(r);
