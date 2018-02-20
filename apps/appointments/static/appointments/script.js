(function( $ ){
    $.fn.getAppointments = function(e) {
        if (e) {
            $.ajax({
                method: "get",
                url: '/search',
                data: ((e).serialize()),
                success: function(res) {
                    var output="<table><thead><tr><th>Date</th><th>Time</th><th>Description</th></thead><tbody>";
                    for (var i in res)
                        {
                            output+="<tr><td>" + res[i].formDate + "</td><td>" + res[i].formTime + "</td><td>" + res[i].description + "</td></tr>";
                        }
                    output+="</tbody></table>";
                    $("#appointments").html(output);
                }
            })
        }
        else {
            $.ajax({
                method: 'get',
                url: '/all_appointments',
                // no data submitted in request
                success: function(res) {
                    var output="<table><thead><tr><th>Date</th><th>Time</th><th>Description</th></thead><tbody>";
                    for (var i in res)
                        {
                            output+="<tr><td>" + res[i].formDate + "</td><td>" + res[i].formTime + "</td><td>" + res[i].description + "</td></tr>";
                        }
                    output+="</tbody></table>";
                    $("#appointments").html(output);
                }
            })
        }
    }; 
})( jQuery );
(function( $ ){
    $.fn.submitAppointment = function() {
        $.ajax({
            method: "post",
            url: $(this).action,
            data: $(this).serialize(),
            success: function(serverResponse) {
                $('#appointments').html('')
            }
        })
    }; 
})( jQuery );

$(document).ready(function(){    
    $("#newAppointmentFormI").hide();
    $('#appointments').getAppointments();
});

$("#showAppointmentForm").click(function(e){
    e.preventDefault();
    $("#newAppointmentFormO").hide();
    $("#newAppointmentFormI").show();
});
$("#hideAppointmentForm").click(function(e){
    e.preventDefault();
    $("#newAppointmentFormI").hide();
    $("#newAppointmentFormO").show();
});
$("#submitNewAppointment").submit(function(e){
    e.preventDefault();
    submitAppointment(e);
});
$("#searchAppointments").submit(function(e){
    e.preventDefault();
    $('#appointments').getAppointments($(this));
});