function getVal() {
  const val = document.getElementById('userName').value;
  console.log(val);
}
getVal()
function getpass() {
  const val = document.getElementById('pass').value;
  console.log(val);
}
//getpass();

function show() {
    let x = document.getElementById('pass')
    if(x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function checkLogin() {
  let userName = document.getElementById('userName')
  let pass = document.getElementById('pass')
  console.log(userName.value, pass.value);

  if(userName.value && pass.value) {
    alert("Welcome");
  } else {
    alert("Wrong password or login id")
  }
}

