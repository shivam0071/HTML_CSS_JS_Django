name = prompt("Enter Your First Name");
last = prompt("Enter Your Last Name")
age = prompt("Enter Your age");
height = prompt("Enter Your Heght");
pet = prompt("Enter Your Pet Name");

if (name[0] == last[0] && age > 20 && age < 30 && height >= 170 && pet[pet.length - 1])
{
console.log('Success');
console.log(name,last,age,height,pet);
}
else {
  console.log('Failed');
}
