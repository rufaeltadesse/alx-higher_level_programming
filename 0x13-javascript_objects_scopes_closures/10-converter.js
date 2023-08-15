#!/usr/bin/node
exports.converter = function (base) {
  function convertBase (n) {
    return n.toString(base);
  }
  return convertBase;
};
