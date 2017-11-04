'use strict';

var outputquery = [];

$(document).ready(function() {
  $('.js-basic-multiple').select2();
  $("#jump").click(function () {
    $.merge(outputquery, $("#idOS").val());
    $.merge(outputquery, $("#idLang").val());
    $.merge(outputquery, $("#idProg").val());
    $.merge(outputquery, $("#idConcep").val());
    $.merge(outputquery, $("#idOthers").val());
  });
});

d3.csv("../data/tags.csv", function (data) {

  data.forEach(function (element) {

    // Creating an option
    var opt = document.createElement("option");
    opt.value = element.id;
    opt.innerHTML = element.tag_name;

    // Appending the option to the appropriate drowdown
    if (element.class == "OS"){
      document.getElementById("idOS").appendChild(opt);
    }
    else if (element.class == "Language"){
      document.getElementById("idLang").appendChild(opt);
    }
    else if (element.class == "Package"){
      document.getElementById("idProg").appendChild(opt);
    }
    else if (element.class == "Feature"){
      document.getElementById("idConcep").appendChild(opt);
    }
    else{
      document.getElementById("idOthers").appendChild(opt);
    }
  });

});
