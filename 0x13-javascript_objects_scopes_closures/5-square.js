#!/usr/bin/node

/* Class square inherits from class Rectangle */
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
