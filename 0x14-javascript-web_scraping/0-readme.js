#!/usr/bin/node
var path = process.argv[2];
var fs = require('fs');
fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        console.log(data);
    } else {
        console.log(err);
    }
});
