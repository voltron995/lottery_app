$(document).ready(function() {
    $('#choose_winners').click(function() {
        $.ajax({
            url: '/users/winners',
            dataType: 'json',
            success: function (result) {
                result = result["users"];
                $("#list1").html(result[0]);
                $("#list2").text(result[1]);
                $("#list3").text(result[2]);
            }
       });
    });
});
