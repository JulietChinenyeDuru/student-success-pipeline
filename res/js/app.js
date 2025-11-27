function validateForm() {
   let firstName = document.forms["loginForm"]["firstName"].value;
   let lastName = document.forms["loginForm"]["lastName"].value;
   let phone = document.forms["loginForm"]["phone"].value;
   let address = document.forms["loginForm"]["address"].value;
   let city = document.forms["loginForm"]["city"].value;
   let country = document.forms["loginForm"]["country"].value;
   let alphabets =  /^[A-Za-z ]+$/;

   if (firstName == "" || firstName == null ) {
      document.getElementById("nameError").innerHTML = "*required";
      return false;
   }else if (lastName == "" || lastName == null) {
      document.getElementById("LastnameError").innerHTML = "*required";
      return false;   
   }else if (!(firstName.match(alphabets)) ) {
      document.getElementById("nameError").innerHTML = "sorry only alphabets are allowed in name field";
      return false;
   }else if (!(lastName.match(alphabets))) {
      document.getElementById("LastnameError").innerHTML = "sorry only alphabets are allowed in name field";
      return false;
   }else if(firstName.length < 5 ){
      document.getElementById("nameError").innerHTML = "Name must be 5 characters and above";
      return false;
   }else if (lastName.length < 5) {
      document.getElementById("LastnameError").innerHTML = "Name must be 5 characters and above";   
   }else if (phone == "" || phone == null) {
      document.getElementById("phoneError").innerHTML = "*required";
      return false;
   }else if (isNaN(phone)) {
      document.getElementById("phoneError").innerHTML = "Please enter a valid number";
      return false;
   }else if (address == "" || address == null) {
      document.getElementById("addressError").innerHTML = "*required";
      return false;
   }else if(address < 8 ){
      document.getElementById("addressError").innerHTML = "address must be 8 characters and above";
      return false;
   }else if (city == "" || city == null) {
      document.getElementById("cityError").innerHTML = "*required";
      return false;
   }else if(city < 3 ){
      document.getElementById("cityError").innerHTML = "city must be 3 characters and above";
      return false;
   }else if (country == "" || city == null) {
      document.getElementById("cityError").innerHTML = "*required";
      return false;
   }else if(country < 3 ){
      document.getElementById("cityError").innerHTML = "country must be 8 characters and above";
      return false;
      
   }
   else{
      setTimeout(function(){
         window.location="index.html";
      },1000)
      alert("Registration Successful...")
   }
}

function validateContact() {
   let firstName = document.forms["contactForm"]["firstName"].value;
   let lastName = document.forms["contactForm"]["lastName"].value;
   let email = document.forms["contactForm"]["email"].value;
   let alphabets =  /^[A-Za-z ]+$/;

   if (firstName == "" || firstName == null ) {
      document.getElementById("error").innerHTML = "*required";
      return false;
   }else if (lastName == "" || lastName == null) {
      document.getElementById("lastError").innerHTML = "*required";
      return false;   
   }else if (!(firstName.match(alphabets)) ) {
      document.getElementById("error").innerHTML = "sorry only alphabets are allowed in name field";
      return false;
   }else if (!(lastName.match(alphabets))) {
      document.getElementById("lastError").innerHTML = "sorry only alphabets are allowed in name field";
      return false;
   }else if(firstName.length < 5 ){
      document.getElementById("error").innerHTML = "Name must be 5 characters and above";
      return false;
   }else if (lastName.length < 5) {
      document.getElementById("lastError").innerHTML = "Name must be 5 characters and above";   
   }else if (email == "" || email == null) {
      document.getElementById("emailError").innerHTML = "*required";
      return false   
   }
   else{
      setTimeout(function(){
         window.location="index.html";
      },1000)
      alert("We will Contact You Soon")
   }
}

cart = () => {

   let currentCart = parseInt(document.getElementById('cart').innerHTML);
   currentCart = currentCart+1
   document.getElementById('cart').innerHTML = currentCart;

   // for (i = 1; i <= count; i++) {
   //    document.getElementById('cart').innerHTML = i++
   //  }
}
