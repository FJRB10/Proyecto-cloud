
function abrirVentana() {
  var ventana = document.getElementById("ventana-Signin");
  ventana.style.display = "flex"; // Mostrar la ventana emergente
}
function irAPaginaSesion() {
  window.location.href = "Login.html";
}
function irAPaginaCrear() {
  window.location.href = "Registro.html";
}
function cerrarVentana() {
  var ventana = document.getElementById("ventana-Signin");
  ventana.style.display = "none"; // Ocultar la ventana emergente
}
