
$(document).ready(function() {
    $.ajax({
        method: 'POST',
        url: '',
        // data: {'yourJavaScriptArrayKey': yourJavaScriptArray},
        success: function (data) {
             //this gets called when server returns an OK response
             alert("it worked!");
        },
        error: function (data) {
             alert("it didnt work");
        }
    });
});
