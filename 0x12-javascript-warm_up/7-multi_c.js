#!/usr/bin/node
const times = process.argv[2];
if (isNaN(times)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
for (let i = 0; i < times; i++) {
  console.log('C is fun');
}
