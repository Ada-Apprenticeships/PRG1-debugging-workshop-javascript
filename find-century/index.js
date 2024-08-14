function findCentury(year) {
  const century = Math.floor((year - 1) / 100) + 1;
  return century + getOrdinalSuffix(century);
}

function getOrdinalSuffix(n) {
  const lastDigit = n % 10;
 
  if (lastDigit === 1) {
    return 'st';
  } else if (lastDigit === 2) {
    return 'nd';
  } else if (lastDigit === 3) {
    return 'rd';
  } else {
    return 'th';
  }
}


console.log(findCentury(1066)); // <-- should be in the "11st century"
