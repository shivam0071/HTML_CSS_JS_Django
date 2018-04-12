console.log('Connected');

headOne = document.querySelector('#one')
headTwo = document.querySelector('#two')
headThree = document.querySelector('#three')


headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Bitcoin is the future";
  headOne.style.color = "red";
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "1.)Hover:-Bitcoin is the Cr%p";
  headOne.style.color = 'black';
})

headTwo.addEventListener('click',function(){
  headTwo.textContent = "lol bch please!!";
  headTwo.style.color = "blue";
})


headThree.addEventListener('dblclick',function(){
  headThree.textContent = "I have a demo account";
  headThree.style.color = "green";
})
