$(document).ready(function () {
    let table = $(".dt-table").DataTable({
        "pageLength": 5,
        lengthMenu: [
            [5, 10, 25, 50],
            [5, 10, 25, 50]
        ],
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/2.0.3/i18n/es-ES.json"
        },
        "columnDefs": [
            { "orderable": false, targets: [-1] },
            { "searchable": false, targets: [-1] },
        ]
    });
});