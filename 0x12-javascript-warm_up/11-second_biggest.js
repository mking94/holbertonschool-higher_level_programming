#!/usr/bin/node
const tab = process.argv;
if (tab.length < 3) {
  console.log('0');
  process.exit(1);
}
tab.sort(function (a, b){
return a - b ;
});
console.log(tab[tab.length - 2]);

