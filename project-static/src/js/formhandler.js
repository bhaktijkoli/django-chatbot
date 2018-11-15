window.fh = {
  handle_error: function(res) {
    switch(res.status) {
      case 400: {
        res.data.forEach(function(el){
          console.log(el);
        })
      }
    }
  },
  set_error: function(el, error) {

  }
}
