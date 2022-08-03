#!/usr/bin/node

if (Number(process.argv[2])) {
  console.log(factorial(process.argv[2]));
} else {
  console.log('1');
}

function factorial (n) {
  if (!n || n < 2) {
    return 1;
  }
  return (n * factorial(n - 1));
}
