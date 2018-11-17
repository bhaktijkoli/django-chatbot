let token = document.head.querySelector('meta[name="csrf-token"]');
if(token) {
  axios.defaults.headers.post['X-CSRFToken'] = token.content;
}

(function() {
  let scrollRevealOptions = {
    distance: '10px',
  }
  ScrollReveal().reveal('.rv', scrollRevealOptions)
  if(document.getElementsByClassName('nav-transparent').length === 1) {
    window.addEventListener('scroll', function(e){
      if(window.scrollY > 70) {
        document.getElementById('navbar').className = "nav-raised";
      } else {
        document.getElementById('navbar').className = "nav-transparent";
      }
    });
  }
})();


let signupForm = document.getElementById('signup_form');
if(signupForm) {
  signupForm.addEventListener("submit", function(e) {
    e.preventDefault();
    let firstname = document.getElementById('firstname');
    let lastname = document.getElementById('lastname');
    let email = document.getElementById('email');
    let password = document.getElementById('password');
    let data = {
      firstname: firstname.value,
      lastname: lastname.value,
      email: email.value,
      password: password.value,
    }
    fh.remove_all_errros(signupForm)
    axios.post("/api/v1/auth/jwt/register", data).then(res=>{
      alert("Success");
    }).catch(res=>{
      res = res.response;
      fh.handle_error(res);
    })
  });
}

let loginForm = document.getElementById('login_form');
if(loginForm) {
  loginForm.addEventListener("submit", function(e) {
    e.preventDefault();
    let email = document.getElementById('email');
    let password = document.getElementById('password');
    let csrf_token = document.getElementById('csrf_token');
    let data = {
      email: email.value,
      password: password.value,
    }
    fh.remove_all_errros(loginForm)
    axios.post("/loginsession/", data).then(res=>{
    }).catch(res=>{
      res = res.response;
      fh.handle_error(res);
    })
  });
}
