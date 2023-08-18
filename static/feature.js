console.log('hhhhhh')
document.addEventListener("DOMContentLoaded", function () {
    // Your JavaScript code here
    window.onscroll = function () {
        myFunction();
    }

    var navbar = document.querySelector(".navbar");
    var sticky = navbar.offsetTop;
      function myFunction() {
        if (window.scrollY > sticky ) {
            navbar.classList.add("sticky")
        } else {
            navbar.classList.remove("sticky");
        }
    }
})
