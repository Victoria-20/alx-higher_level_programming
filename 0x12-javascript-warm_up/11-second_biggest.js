#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let array = process.argv.filter(elem => parseInt(elem));
  array = array.filter(elem => elem < Math.max(...array));
  console.log(Math.max(...array));
}
