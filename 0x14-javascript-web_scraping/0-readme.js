#!/usr/bin/node
const fs = require('fs');
fs.readfile(process.argv[2], 'utf', function(error, content){
    console.log(error || content);
});
