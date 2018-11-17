let lastButton = null;
window.fh = {
  handle_error: function(res) {
    fh.remove_all_errros(signupForm);
    switch(res.status) {
      case 400: {
        Object.entries(res.data).forEach(function(el){
          let element = el[0];
          let msg = el[1][0];
          fh.set_error(element, msg)
        })
      }
    }
    fh.show_button();
  },
  set_error: function(element, msg) {
    let group = document.querySelector("#"+element).closest('.input-group');
    let helpblock = group.querySelector('.help-block');
    helpblock.innerHTML = msg;
    helpblock.classList.add('error')
    group.classList.add('error')
  },
  remove_all_errros: function(form) {
    form.querySelectorAll(".input-group").forEach(function(group) {
      group.classList.remove('error');
      let helpblock = group.querySelector('.help-block');
      if(helpblock) {
        helpblock.classList.remove('error');
        helpblock.innerHTML=" ";
      }
    })
  },
  hide_button: function() {
    lastButton = document.activeElement;
    lastButton.classList.add('running')
    lastButton.disabled = true;
  },
  show_button: function() {
    lastButton.disabled = false;
    lastButton.classList.remove('running');
  }
}
