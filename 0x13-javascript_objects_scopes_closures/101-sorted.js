#!/usr/bin/node
const existing = require('./101-data').dict;
const myDictionary = {};
Object.keys(existing).map(function (key) {
  if (!Array.isArray(myDictionary[existing[key]])) {
    myDictionary[existing[key]] = [];
  }
  myDictionary[existing[key]].push(key);
});

console.log(myDictionary);
