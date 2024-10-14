export function mostrarMenu(e) {
    // if (e.target.classList.contains("toggle-btn")) {
    //     document.querySelector("#sidebar").classList.toggle("expand");
    // }

    if (e.target.closest(".toggle-btn")) {
        document.querySelector("#sidebar").classList.toggle("expand");
    }
}

