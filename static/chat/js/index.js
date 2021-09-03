//Форматирование инпута для названия чата
input = document.getElementById('chat-name-input')
input.addEventListener('input', function(){
  this.value = this.value.replace(/[^\x00-\x7F]+/ig,  '')
  this.value = this.value.replace(' ', '')
});
