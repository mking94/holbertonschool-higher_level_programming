#!/usr/bin/node

const axios = require('axios');
let count = 0;
axios({
  method: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/'
}).then(res => {
  if (res) {
    let i = 0;
    while(res.data.results[i])
    {
        let j = 0;
        while(res.data.results[i].characters[j])
        {
            let req = require('axios');
            axios({
                method: 'GET',
                url: characters[j] 
            }).then(res => {
                if(res.data.name == "Wedge Antilles")
                {
                    count++;
                }
            })
            j++;
        }
    }
  }
});
console.log(count);
