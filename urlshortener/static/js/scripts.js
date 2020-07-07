function myFunction() {
  document.getElementById("myInput").select();;
  document.execCommand("copy");
  var div = document.getElementById("myBtn");
  div.classList.remove(div.classList[2])
  const classss = ["btn-danger", "btn-succes", "btn-info", "btn-dark", "btn-warning", "btn-secondary", "btn-primary"]
  const rndclass = classss[Math.floor(Math.random() * classss.length)];
  div.classList.toggle(rndclass);
}
