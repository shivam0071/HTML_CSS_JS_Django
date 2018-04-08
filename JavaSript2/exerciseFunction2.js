function sleepIn(weekday, vacation) {
  var sleep = false
  if (! weekday || vacation)
  {
    sleep = true
  }
  console.log(sleep);
  return sleep
}
sleepIn(false , true)


function monkeySmile(aSmile, bSmile) {
  var trouble = false
  if (aSmile && bSmile || !aSmile && !bSmile)
  {
    trouble = true;
  }
  console.log(trouble);
  return trouble;
}

monkeySmile(true, false)

function stringTimes(str, n) {
  var temp = str
  while (n > 1)
  {
  temp = temp+str
  n -= 1
  }
  console.log(temp);
}
stringTimes("H", 5);


function luckySum(a ,b ,c) {
var sum = 0;
if (a !== 13 )
  {
  if (b !== 13)
    {
      if (c === 13)
      {
         sum = a+b;
      }
      else {
        sum = a+b+c;
      }
    }
  else {
    sum = a;
  }
    }
else {
    sum = 0;
  }

console.log(sum);
}

luckySum(1,13,5)



//small = 3  big = 1  goal =  10
function makeBricks(small ,big, goal) {
  possible = false;
  if (big * 5 === goal || small * 1 === goal || small * 1 + big * 5 === goal)
    {possible = true;}
  console.log(possible);
  return big * 5 === goal || small * 1 === goal || small * 1 + big * 5 === goal
}

makeBricks(3,2,10)
