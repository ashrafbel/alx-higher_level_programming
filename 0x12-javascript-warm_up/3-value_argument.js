#!/usr/bin/node
// This line defines the path to the interpreter that will execute the script

if (process.argv[2] === undefined) {
  console.log('No argument');

} else {
  console.log(process.argv[2]);
}
