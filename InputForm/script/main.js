'use strict';

var outputquery = [];  // Will be fed to our search engine

// Will be fired once the DOM is loaded
$(document).ready(function() {

  // Giving all drop downs of class '.js-basic-multiple' Select2 Functionality
  $('#idOS').select2({maximumSelectionLength: 3});
  $("#idLang").select2({maximumSelectionLength: 1});
  $('#idProg').select2({maximumSelectionLength: 3});
  $('#idConcep').select2({maximumSelectionLength: 3});
  $('#idOthers').select2({maximumSelectionLength: 3});

  // merging all the selected tags to "outputquery"
  $("#jump").click(function () {
    $.merge(outputquery, $("#idOS").val());  // One by one merging all the selected tags to "outputquery"
    $.merge(outputquery, $("#idLang").val());  // "  "  "
    $.merge(outputquery, $("#idProg").val());  // "  "  "
    $.merge(outputquery, $("#idConcep").val());  // "  "  "
    $.merge(outputquery, $("#idOthers").val());  // One by one merging all the selected tags to "outputquery"
  });

  // Suggestion loader
  $("#firstloader").click(ajax_suggest_sender);

  // Loading Tags file and appending options to appropriate drop-down
  d3.csv("../data/tags.csv", function (data) {
    data.forEach(function (element) {
      // Creating an option
      var opt = document.createElement("option");
      opt.value = element.id;
      opt.innerHTML = element.tag_name;
      // Appending the option to the appropriate drowdown
      if (element.class == "OS"){document.getElementById("idOS").appendChild(opt);}
      else if (element.class == "Language"){document.getElementById("idLang").appendChild(opt);}
      else if (element.class == "Package"){document.getElementById("idProg").appendChild(opt);}
      else if (element.class == "Feature"){document.getElementById("idConcep").appendChild(opt);}
      else{document.getElementById("idOthers").appendChild(opt);}
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

// Promisifying AJAX request
function promise_ajax(query_tag, tag_type){
  return new Promise(function (resolve, reject) {
    // Creating a new AJAX request
    var html_request = new XMLHttpRequest();
    // Setting request parameters
    var query_added = "MATCH p = (source:SOTag{Title: '" + query_tag + "'})-[:Connects*1..1]-(target:SOTag{Class: '" + tag_type + "'}) RETURN target.Title as Neighbour ORDER BY relationships(p)[0].Weight desc limit 5;";
    var params = JSON.stringify({
      "query" : query_added,
      "params" : {}
    });
    // Setting URL of server and request type
    html_request.open("POST", "http://localhost:7474/db/data/cypher");
    // What will happen when the request is loaded?
    html_request.onload = function () {
      if (html_request.status >= 200 && html_request.status < 400){
        resolve(JSON.parse(html_request.responseText).data);
      } else{
        console.error(html_request.status + "| Connected to the server but server gave some error.");
      };
    };
    // Sending content format to server to tell it about the data it should accept
    html_request.setRequestHeader("Content-Type", "application/json");
    // Sending content format to the server to tell it what kind of data the client accepts
    html_request.setRequestHeader("Accept", "application/json");
    // If the request fails due to error on client side
    html_request.onerror = function () {
      console.error("Server Connection Error");
    };
    // Send the HTTP request
    html_request.send(params);
  });
}

// Sends a notification when data load is successful.
function notify_me(message_string){
	  // Let's check if the browser supports notifications
	  if (!("Notification" in window)) {alert(message_string);}
	  // Let's check whether notification permissions have already been granted
	  else if (Notification.permission === "granted") {
		    // If it's okay let's create a notification
		  var notification = new Notification(message_string);
	  }
	  // Otherwise, we need to ask the user for permission
	  else if (Notification.permission !== "denied") {
		    Notification.requestPermission(function (permission) {
	          if (permission === "granted") { // If the user accepts, let's create a notification
			        var notification = new Notification(message_string);
	          }
            else{
              console.log(message_string);
            }
	      });
	  }
}

// Sending request and fetching suggestions
function ajax_suggest_sender(out_features, out_packages, out_mixedbag) {

  var in_OS_Val = $("#idOS").val();
  var in_Lang_Val = $("#idLang").val();
  var in_Package_Val = $("#idProg").val();
  var in_Concepts_Val = $("#idConcep").val();
  var in_Others_Val = $("#idOthers").val();

  var in_Lang_txt = $("#idLang option[value='" + in_Lang_Val[0] + "']").text();

  var in_Concepts_txt = [];
  for (var i = 0; i < in_Concepts_Val.length; i++){
    in_Concepts_txt.push($("#idConcep option[value='" + in_Lang_Val[i] + "']").text());
  }

  if (in_Lang_Val.length == 0 || in_Concepts_Val.length == 0){
    notify_me("Select a Language Tag and some Feature Tags first.");
    return 0;
  }
  else{
      promise_ajax(in_Lang_txt, "Feature").then(function (response) {
        out_features.concat(response);
      });
      promise_ajax(in_Lang_txt, "Package").then(function (response) {
        out_packages.concat(response);
      });
      promise_ajax(in_Lang_txt, "ND").then(function (response) {
        out_mixedbag.concat(response);
      });
      for (var i = 0; i < in_Concepts_Val.length; i++){
        promise_ajax(in_Concepts_txt[i], "Feature").then(function (response) {
          out_features.concat(response);
        });
        promise_ajax(in_Concepts_txt[i], "Package").then(function (response) {
          out_packages.concat(response);
        });
        promise_ajax(in_Concepts_txt[i], "ND").then(function (response) {
          out_mixedbag.concat(response);
        });
      }
  }

}
