/**
 * Add a required class to labels whose inputs, selects, or textareas have a required
 * attribute.
 */
function addRequiredClassToLabels() {
  var requiredInputSelectTextareas = document.querySelectorAll('input[required]:not([type="checkbox"]),select[required],textarea[required]');

  for (var i = 0; i < requiredInputSelectTextareas.length; i++) {
    var requiredInputSelectTextarea = requiredInputSelectTextareas[i];
    var parent = requiredInputSelectTextarea.parentElement;
    var label = parent.querySelector('label');

    if (label !== null) {
      label.classList.add('required');
    }
  }
}

/**
 * Add the 'active' class to each selector if the subject in location.href
 */
function addActiveClassToSelector(selector) {
  var links = document.querySelectorAll(selector);

  for (var i = 0; i < links.length; i++) {
    var link = links[i];
    var subject = link.dataset.subject;

    if (link.href === location.href || (subject !== undefined && location.href.split('?')[0].includes(subject))){
      link.classList.add('active');
    }
  }
}

addRequiredClassToLabels();
addActiveClassToSelector('#sidebar .nav-link');
addActiveClassToSelector('.navbar-nav .nav-link');

$('.datepicker').datepicker();
