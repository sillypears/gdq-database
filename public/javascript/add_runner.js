$(function(){
    console.log("hi");  
    $('#submit_runner').click(function(){
        
        name = $('#name').val();
        d_name = $('#display_name').val();
        twitch = $('#twitch').val();
        twitter = $('#twitter').val();
        youtube = $('#youtube').val();
        console.log("Adding " + d_name + " as " + name + " with " + twitch + ", " + twitter + " and " + youtube);
    //    $('#display_name').val(selected.data('display_name'))
    //    $('#twitch').val(selected.data('twitch'));
    //    $('#twitter').val(selected.data('twitter'));
    //    $('#youtube').val(selected.data('youtube'));
    });
});