var hiddenBody = document.querySelector('input[name="body"]');

var summernote = $('#body').summernote();

var noteEditable = document.querySelector('.note-editable');
var noteCodeable = document.querySelector('.note-codable');

noteEditable.addEventListener('keyup', function() {
  var code = $('#body').summernote('code');
  hiddenBody.value = code;
});

noteCodeable.addEventListener('keyup', function() {
  var code = this.value;
  hiddenBody.value = code;
});


