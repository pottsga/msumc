$(document).ready(function() {
  var body = document.querySelector('#body');
  var hiddenBody = document.querySelector('input[name="body"]');
  var originalHTML = body.dataset.html;
  hiddenBody.value = originalHTML;

  var summernote = $('#body').summernote('code', originalHTML);

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
});
