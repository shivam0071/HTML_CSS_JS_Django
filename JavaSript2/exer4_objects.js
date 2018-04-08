alert('hi')

var employee ={
  name: 'Agent Smith',
  job : 'Spy',
  age : 31
}


function nameLength(name) {
  console.log(name.length - 1);
  alert('length of his name is '+(name.length - 1))
  return name.length -1 ;
}


function lastName(name) {
  alert('his last name is '+name.split(' ')[1])
}

function addAttrib(key,value) {
 employee[key] = value
  alert('Added '+key+' '+value)
  console.log(employee);
}

function display() {
  console.log('Name is '+employee['name']+' job is '+employee['job']+' and age is '+employee['age']);
}
nameLength(employee['name'])
lastName(employee['name'])
addAttrib('Sex', 'M')
display()



// notice there is now "" in object keys but we need them while accessing
