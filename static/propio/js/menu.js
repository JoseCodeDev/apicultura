// Menu desplegable
const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
    document.querySelector("#sidebar").classList.toggle("expand");
});


// Alerta para decir si quiero elimibar algo
// Swal.fire({
//     title: "Are you sure?",
//     text: "You won't be able to revert this!",
//     icon: "warning",
//     showCancelButton: true,
//     confirmButtonColor: "#3085d6",
//     cancelButtonColor: "#d33",
//     confirmButtonText: "Yes, delete it!"
// }).then((result) => {
//     if (result.isConfirmed) {
//         Swal.fire({
//             title: "Deleted!",
//             text: "Your file has been deleted.",
//             icon: "success"
//         });
//     }
// });