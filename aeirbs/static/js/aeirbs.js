$(document).ready(function() {
    $('.table').DataTable({
        "pagingType": "first_last_numbers",
        searching: false,
    });

    $(".dataTables_paginate").addClass("btn btn-sm");
});