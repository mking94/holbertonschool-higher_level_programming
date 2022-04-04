#!/usr/bin/node
const n = process.argv[2];
const r = 1;
if (isNaN(n)) {
  console.log('1');
  process.exit(1);
}
while (n > 0) r *= n--;
console.log(r);

