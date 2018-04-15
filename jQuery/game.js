player_name = [prompt('Player One Enter your name, you will be blue!')]
player_name.push('blue')
// Player One: It is your turn,please pick up a cloumn to drop your blue chip.
player_name2 = [prompt('Player Two Enter your name, you will be red!')]
player_name2.push('red')

// flag = true;
// function whosTurn() {
//   if ()
//   {
    promt_text = player_name[0]+' it is your turn,please pick up a column to drop your '+player_name[1]+' chips'
//   }
//   else {
//     promt_text = player_name[2]+' it is your turn,please pick up a column to drop your '+player_name[2]+' chips'
//   }
//   flag = false;
// }
// whosTurn()
function demo() {
  console.log('demo');
}

$('h4').text(promt_text);
function row_click() {
  console.log('Clicked');
  console.log(this);
  butt = this.querySelector('button')
  butt.style.background = 'blue';
  // butt.setAttribute('class','blue ')
  // console.log(butt.);
 // for (var i = 0; i < this.length; i++) {
 //
 // }
}

// rows = $('tr')
// console.log(rows);
// rows.on('click',row_click)
// for (var i = 0; i < array.length; i++) {
//   array[i]
// }
column = $('td');
console.log(column);
column.on('click',row_click)
