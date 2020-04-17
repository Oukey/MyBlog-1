    jQuery(document).ready(function($){
        $("#id_model").change(function () {
          var url = $("#selectAutoForm").attr("data-cities-url-modyfy");  // get the url of the `load_cities` view
          var modelId = $(this).val();  // get the selected country ID from the HTML input

          $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
              'model': modelId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
              $("#id_modyfy").html(data);  // replace the contents of the city input with the data that came from the server
            }
          });

        });
    });
