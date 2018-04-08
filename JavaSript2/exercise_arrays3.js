var roster = [];

function add(name) {
roster.push(name);
}

function remove(name) {
index = roster.indexOf(name);
if (index > -1)
  {
  roster.splice(index,1);  //  1 tells how many elements to remove
  }
}

function display() {
  console.log(roster);
}

alert('Hi Wadecum to the array of names')
while(true)
{
response =prompt('Type one of these to do them \n 1.)Add 2.) Remove 3.)Display 4.) Quit').toLowerCase();
if (response === 'add' || response === 'a')
  {
    var name = prompt('Enter a name please!!')
    add(name)
  }

else if (response === 'display' || response === 'd')
    {
    display()
    }
else if (response === 'quit' || response === 'q')
  {
  alert('Thanks for making it to the array')
  break;
  }
else
{
name = prompt('Enter a name to remove it');
remove(name);
}
}
