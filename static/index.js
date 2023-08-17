function getVal() {
  const val = document.getElementById('userName').value;
  console.log(val);
}
getVal()
function getpass() {
  const val = document.getElementById('pass').value;
  console.log(val);
}
getpass();

function show() {
    let x = document.getElementById('pass')
    if(x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function checkLogin() {
  const userName = document.getElementById('userName').value;
  const pass = document.getElementById('pass').value;
  console.log(userName, pass);

//   if(userName == 46 && pass == 46) {
//     alert("Welcome");
//   } else {
//     alert("Wrong password or login id")
//   }
}

