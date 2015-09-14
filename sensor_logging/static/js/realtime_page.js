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

window.onload = function(){
    document.getElementById('chart1').style.display = 'none';
    document.getElementById('chart2').style.display = 'none';
    document.getElementById('chart3').style.display = 'none';
    document.getElementById('chart4').style.display = 'none';

    //document.getElementById('1').checked = false;
    //document.getElementById('2').checked = false;
    document.getElementById('3').checked = false;
    //document.getElementById('4').checked = false;

    $("#range").ionRangeSlider({
        grid: true,
        min: 0,
        max: 24,
        from: 2
    });
};

$(function () {
    var intervals = {};
    $('input').on('click', function () {
        var elem_val = $(this).val();
        var chart_id = 'chart' + elem_val;
        if (is_checked(elem_val)) {
            document.getElementById(chart_id).style.display = 'block';
            intervals[elem_val] = setInterval( function(){plot_realtime(elem_val, get_time_frame())}, 6000);
        }
        else {
            clearInterval(intervals[elem_val]);
            document.getElementById(chart_id).style.display = 'none';
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
    //console.log(slider.old_from);
    return slider.old_from;
}