#!/usr/bin/node
<<<<<<< HEAD
let n = process.argv[2];
let r = 1;
=======
const n = process.argv[2];
const r = 1;
>>>>>>> e6a4af98b6c53584ac45d9656c7416f2a5b99b07
if (isNaN(n)) {
  console.log('1');
  process.exit(1);
}
<<<<<<< HEAD
n = Number(n);
while (n > 0) r *= n--;
console.log(r);
=======
while (n > 0) r *= n--;
console.log(r);

>>>>>>> e6a4af98b6c53584ac45d9656c7416f2a5b99b07
