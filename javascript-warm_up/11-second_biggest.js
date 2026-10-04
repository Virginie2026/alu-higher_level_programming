#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);
  console.log(uniqueSorted[1] !== undefined ? uniqueSorted[1] : 0);
}
