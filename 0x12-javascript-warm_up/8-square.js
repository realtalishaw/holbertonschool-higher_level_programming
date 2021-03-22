#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    let i;
    let j;
    let out = '';
    for (i = 0; i < size; i++) {
      for (j = 0; j < size; j++) {
        out += 'X';
      }
      console.log(out);
      out = '';
    }
  }
}
