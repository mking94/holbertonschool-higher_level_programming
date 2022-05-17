#!/usr/bin/node

const axios = require('axios');
let tab;
async function start()
{
await axios({
  method: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/'
}).then(res => {
  if (res) {
   tab = res.data.results; 
}
});


link = [];
let i = 0;
while(tab[i])
{
link = link.concat(tab[i].characters);
i++;
}

var count = link.reduce((acc,curr) => {
    if(curr.endsWith("/18/"))
       acc++;
    return acc;
},0);

console.log(count);
}

start();
