$(document).ready(function () {
    $('#grid_inbox').hide();
    $('#grid_home').show();
    $('#grid_spam').hide();

    $('#a1').click(function (e) {

        e.preventDefault();
        $('#grid_inbox').hide();
        $('#grid_home').show();
        $('#grid_spam').hide();
    });
    $('#a2').click(function (e) {

        e.preventDefault();
        $('#grid_inbox').show();
        $('#grid_home').hide();
        $('#grid_spam').hide();
    });
    $('#a3').click(function (e) {

        e.preventDefault();
        $('#grid_inbox').hide();
        $('#grid_home').hide();
        $('#grid_spam').show();
    });

});