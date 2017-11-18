'use strict';

var outputquery = [];  // Will be fed to our search engine

// Will be fired once the DOM is loaded
$(document).ready(function() {

  // Giving all drop downs of class '.js-basic-multiple' Select2 Functionality
  $('.js-basic-multiple').select2();

  // merging all the selected tags to "outputquery"
  $("#jump").click(function () {
    $.merge(outputquery, $("#idOS").val());  // One by one merging all the selected tags to "outputquery"
    $.merge(outputquery, $("#idLang").val());  // "  "  "
    $.merge(outputquery, $("#idProg").val());  // "  "  "
    $.merge(outputquery, $("#idConcep").val());  // "  "  "
    $.merge(outputquery, $("#idOthers").val());  // One by one merging all the selected tags to "outputquery"
  });

  // Loading Tags file and appending options to appropriate drop-down
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

  // Adding drag/drop event listeners along with the response functions
  $(".draggableEle").on("dragstart", function (event) {
    // event.originalEvent.dataTransfer instead of event.dataTransfer
    // because jQuery only pass jQuery event object not the browser event object
    event.originalEvent.dataTransfer.setData("tagsdata", event.target.textContent);
  });

  $("#dragdiv").on("dragover", function (event) {
    event.preventDefault();  // By default, data/elements cannot be dropped in
    // other elements
  });

  $("#dragdiv").on("drop", function (event) {
    event.preventDefault();  // Default action is to open data as a link
    var data = event.originalEvent.dataTransfer.getData("tagsdata");
    $("#innerdragdiv").append("<li class='list-group-item'>" + data + " <span class='badge'>X</span>" +"</li>");  // Appending the suggestion selected
    $("#innerdragdiv").last().on("click", function (spanevent) {  // Adding event listener for removing a picked suggestion
      $(spanevent.target).parent().remove();  // Not including .parent() will just remove the span
    });
  });


});
