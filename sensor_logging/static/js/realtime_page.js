function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$.ajaxSetup({
    error: function(xhr, textStatus, error) {
        console.log(error);
    }
});

// main function
$(function(){

    $("#range").ionRangeSlider({
        grid: true,
        min: 0,
        max: 24,
        from: 2
    });
    $(".chart-div").hide();
    $(".mySwitch").bootstrapSwitch('state', false);

    // switch toggle event
    var intervals = {};
    $(".mySwitch").on('switchChange.bootstrapSwitch', function(event, state) {
        var elem_val = this.id;
        var chart_id = 'chart' + elem_val;
        if (state == true){
            $('#' + chart_id).show('slow');
            setTimeout(function () {
                plot_realtime(elem_val, get_time_frame());
            }, 700);
            intervals[elem_val] = setInterval( function(){plot_realtime(elem_val, get_time_frame())}, 20000);
        }
        if(state == false){
            clearInterval(intervals[elem_val]);
            $('#' + chart_id).hide('slow');
        }
    });

});

function is_checked(elem_id){
    if (document.getElementById(elem_id).checked){
        console.log(elem_id + ' is checked');
        return true;
    }
    else{
        console.log(elem_id + ' is unchecked');
        return false;
    }
}

function get_time_frame(elem_id){
    var slider = $("#range").data("ionRangeSlider");
    return slider.old_from;
}