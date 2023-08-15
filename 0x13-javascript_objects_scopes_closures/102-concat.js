#!/usr/bin/node
const myFile = require('fs');
let content = '';
content = content.concat(myFile.readFileSync(process.argv[2]));
content = content.concat(myFile.readFileSync(process.argv[3]));
myFile.writeFileSync(process.argv[4], content);
