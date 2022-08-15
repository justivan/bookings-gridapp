document.addEventListener("DOMContentLoaded", function () {
  let reservTable = new DataTable("#reservTable", {
    dom: "<Bf>rt<'d-flex justify-content-between mt-3'ip>",
    ajax: "/api/data",
    ordering: false,
    keys: true,
    buttons: ["pageLength"],
    lengthMenu: [
      [25, 50, 75, -1],
      [25, 50, 75, "All"],
    ],
    columns: [
      {
        data: null,
        defaultContent: "",
        render: function () {
          return `<i class="bi bi-plus-circle-fill text-success"></i>`;
        },
        className: "text-center",
        width: 20,
      },
      { data: "statu4" },
      { data: "ref_id" },
      { data: "res_id" },
      { data: "bkg_ref" },
      { data: "opr_code" },
      { data: "opr_name" },
      { data: "hotel_name", className: "ellipsis" },
      { data: "sales_date" },
      { data: "in_date" },
      { data: "out_date" },
      { data: "room", className: "ellipsis" },
      { data: "meal" },
      { data: "days" },
      { data: "adult" },
      { data: "child" },
      { data: "purchase" },
      { data: "sales" },
      { data: "opr_cost" },
      {
        data: null,
        render: function (data, type, row) {
          return Math.round(row.opr_cost - row.sales);
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          return (
            Math.round(((row.sales - row.purchase) / row.sales) * 100) + "%"
          );
        },
      },
      { data: "gwg_p_id" },
      {
        data: "gwg_p_code",
        className: "ellipsis",

        createdCell: function (td, cellData, rowData, row, col) {
          td.setAttribute("data-bs-toggle", "tooltip");
          td.setAttribute("data-bs-title", rowData.gwg_p_name);
        },
      },
      { data: "gwg_s_id" },
      { data: "gwg_s_code", className: "ellipsis" },
    ],
    columnDefs: [
      {
        targets: [8, 9, 10],
        render: $.fn.dataTable.render.intlDateTime("en-GB"),
      },
      {
        targets: [16, 17, 18, 19],
        render: $.fn.dataTable.render.number("", null, 2, null),
        className: "text-end",
        createdCell: function (td, cellData, rowData, row, col) {
          if (cellData == 0 || cellData == "") {
            td.classList.add("bg-danger", "text-dark", "bg-opacity-25");
          }
        },
      },
    ],
    drawCallback: function () {
      const paginationControl = document.querySelector(
        "#reservTable_paginate > ul"
      );
      paginationControl.classList.add("pagination-sm");

      const tooltipTriggerList = document.querySelectorAll(
        '[data-bs-toggle="tooltip"]'
      );
      const tooltipList = [...tooltipTriggerList].map(
        (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
      );
    },
  });

  new $.fn.dataTable.Responsive(reservTable);
});
