// myvariable.textContent - This returns just the text
// myvariable.innerHTML - This returns the actual html
// myvariable.getAttribute() - This returns the original attribute
// myvariable.setAttribute() - This allowed you to set an attribute

// v.innerText
// "I am another header with the special id. FACEBOOK LINK"

// v.textContent
// "I am another header with the special id.
    // FACEBOOK LINK
  // "

// a = v.querySelector('a')
// v = document.querySelector('h4')
// b = a.getAttribute('href')
// a.setAttribute('href','https://www.youtube.com')
// para = document.querySelector('p')
// <p>​…​</p>​
// para
// <p>​…​</p>​"To Edit Styles, we've already seen we can use the .style tag.
//     Now if we want to edit "<strong>​actual html or text​</strong>​" or
//     "<a href=​"http:​/​/​www.google.com">​attributes​</a>​" we can use different methods.
//      If you want to change the text,html content, or attributes you can use the following:
//   "</p>​
// para.textContent = "Bitconneeeeeeeeeeeeeeeeeeett"
// "Bitconneeeeeeeeeeeeeeeeeeett"
// para.textContent = "<strong>Bitconneeeeeeeeeeeeeeeeeeett</stron>"
// "<strong>Bitconneeeeeeeeeeeeeeeeeeett</stron>"
// para.textContent = "<strong>Bitconneeeeeeeeeeeeeeeeeeett</strong>"
// "<strong>Bitconneeeeeeeeeeeeeeeeeeett</strong>"
// para.innerHTML = "<strong>Bitconneeeeeeeeeeeeeeeeeeett</strong>"
// "<strong>Bitconneeeeeeeeeeeeeeeeeeett</strong>"
// the text now is bold
