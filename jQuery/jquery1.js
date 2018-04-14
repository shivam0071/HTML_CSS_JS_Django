// $('h1').css('color' , 'red');

// Events

$('h1').click(function() {
  $('h1').eq(0).text("All Pretty Like")
})


$('h1').eq(1).mouseenter(function() {
  $('h1').eq(1).text("Hey")
})


//Key Press
// $('input').eq(0).keypress(function () {
//   $('p').toggleClass('red_stuff')
// })

//event has various attrb of the event
$('input').eq(0).keypress(function (event) {
  console.log(event);
  if (event.which === 113){ // press q
    $('p').toggleClass('red_stuff');
  }
})


//on method is used to add eventlister like vanilla js

$('h1').eq(0).on('dblclick',function () {
  $('h1').eq(0).text("Jinxxx ")
})


 //Animation n effetcs
$('input').eq(1).click(function (event) {
  $('.container').fadeOut(3000);
})
