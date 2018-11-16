window.fh = {
  handle_error: function(res) {
    switch(res.status) {
      case 400: {
        Object.entries(res.data).forEach(function(el){
          let element = el[0];
          let msg = el[1][0];
          fh.set_error(element, msg)
        })
      }
    }
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
  }
}
