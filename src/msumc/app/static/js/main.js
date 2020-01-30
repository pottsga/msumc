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

/**
 * Ensure the format of the phone number is (000) 000-0000
 */
function addPhoneNumberValidation() {
  var phoneNumbers = document.querySelectorAll('.phone-number');

  console.log(phoneNumbers)

  for (var i = 0; i < phoneNumbers.length; i++) {
    var phoneNumber = phoneNumbers[i];

    phoneNumber.addEventListener('keyup', function() {
      var value = phoneNumber.value;
      var newValue = value;

      if (value[0] !== '(' && value.length === 1) {
        newValue = `(${newValue}`;
      }
      if (value[3] !== ')' && value.length === 4) {
        newValue = `${newValue}) `;
      }
      if (value[4] !== ' ' && value.length === 5) {
        newValue = `${newValue} `;
      }
      if (value[8] !== ' ' && value.length === 9) {
        newValue = `${newValue}-`;
      }
      if (value.length > 14) {
        newValue = value.substring(0, 14);
      }

      phoneNumber.value = newValue;
    });
  }
}

addRequiredClassToLabels();
addPhoneNumberValidation();
addActiveClassToSelector('#sidebar .nav-link');
addActiveClassToSelector('.navbar-nav .nav-link');

$('.datepicker').datepicker();
