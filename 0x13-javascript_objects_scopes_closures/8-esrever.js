#!/usr/bin/node

exports.esrever = function (list) {
// Returns the reversed version of a list
  const reversedList = [];
  let k = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList[k] = list[i];
    k++;
  }
  return (reversedList);
};
