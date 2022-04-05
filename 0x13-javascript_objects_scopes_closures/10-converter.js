#!/usr/bin/node
exports.converter = function (base) {
  function strt (number) {
    return number.toString(base);
  }
  return strt;
};
