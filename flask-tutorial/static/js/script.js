//console.log('Everything is linked and working!!');

var button = document.getElementsByClassName('submit-button-container')[0];

button.addEventListener('mouseover', function(){
  console.log('hello from mr. button!')
  button.style.background = 'blue';
});

button.addEventListener('mouseout', function(){
  console.log('goodbye!')
  button.style.background = 'red';
});


$('.flexdatalist').flexdatalist({
     minLength: 1,
     textProperty: '{titel}',
     valueProperty: 'id',
     selectionRequired: true,
     visibleProperties: ["title"],
     searchIn: 'title',
     data: 'static/movies.json'
});
