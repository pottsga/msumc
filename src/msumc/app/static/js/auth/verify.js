const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const password = form.querySelector('input#password').value;
  const password2 = form.querySelector('input#password2').value;

  console.log(password, password2)

  if (password !== password2) {
    alert('Password must match.');
    return false;
  } 

  form.submit();
});
