
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
function irAPaginaContraseña() {
  window.location.href = "OlvideContra.html";
}
function irAPaginaPerfil() {
  window.location.href = "Perfil.html";
}
function irAPaginaCod1() {
  window.location.href = "Cod1.html";
}
function irAPaginaAnalista() {
  window.location.href = "PrincipalAnalista.html";
}
function cerrarVentana() {
  var ventana = document.getElementById("ventana-Signin");
  ventana.style.display = "none"; // Ocultar la ventana emergente
}

// revisar funcion, resisar si es necesaria
function validarFormulario() {
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;

  if (nombre === "" || email === "") {
      alert("Por favor, completa todos los campos.");
      return false; // Evita que el formulario se envíe
  }

  return true; // Permite que el formulario se envíe
}