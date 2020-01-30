$('#family_datatable').DataTable({
  dom: `
    <'row'<'col-sm-12 pb-3'B>>
    <'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>
    <'row'<'col-sm-12'tr>>
    <'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>
  `,
  buttons: [
    'excel'
  ],
  lengthMenu: [
    [25, 50, 75, -1],
    ['25 rows', '50 rows', '75 rows', 'Show all'],
  ],
  responsive: true,
});
