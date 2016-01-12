(function() {
  $(document).ready(function () {

    var searchBar = $('#search_bar');
    var searchBtn = $('#search_button');
    var alerts = $('#alerts');
    var response = $('#response');

    searchBtn.click(function(event){
      event.preventDefault();
      if(searchBar.val() !== ''){
        queryServer(searchBar.val());
      } else {
        alerts.text('Please enter a search term')
      }
    });

    function queryServer(value){

      // Will query the server with a POST request form zone_query
      // in the format {query_data: value}
      // where value is the search term
      // example:  $.post('index.html', {'query_data': 'Seoul'}
      // this is for testing purpose only

      alerts.text('Queried the server for ' + value);
      $.ajax({
        url: 'zone_query',
        type: 'POST',
        data: value,
        contentType: 'json; charset=utf-8',
        dataType: "json",
        success: function(data){
          console.log(data);
          response.text(data.response);
        }
      })

    }

  });
}());
