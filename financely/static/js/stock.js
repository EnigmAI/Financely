//console.log("add to portfolio")
var updateBtns = document.getElementsByClassName("update-portfolio");


updateBtns[0].addEventListener("click",function(){
  var stock_key = this.dataset.symbol;
  var action = this.dataset.action;
  var name = this.dataset.name;
  console.log(stock_key + "  " + action)
  console.log(name)
  $.ajax({
    type: 'POST',
    url: '',
    data: {
      'myData': stock_key,
      'action': action,
      'name': name,
    'csrfmiddlewaretoken': csrftoken
  },
    success: console.log('success'),
    error: console.log('failure')
  });

})
