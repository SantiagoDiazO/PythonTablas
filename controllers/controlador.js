let boton = document.getElementById('generarboton')
boton.addEventListener("click", function(evento){
    evento.preventDefault()
    //alert("Ahi vamos...")
    let reporte = document.getElementById("reporte")
    reporte.classList.remove("d-none")
})