    jQuery(document).ready(function($){
        $("#id_area").change(function () {
          var url = $("#SelectAreaForm").attr("data-group-url");  // get the url of the `load_cities` view
          var areaId = $(this).val();  // get the selected country ID from the HTML input

          $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/...)
            data: {
              'id_area': areaId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
              $("#id_group_kn").html(data);  // replace the contents of the city input with the data that came from the server
            }
          });

        });
    });
