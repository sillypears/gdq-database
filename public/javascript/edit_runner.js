$(function(){
    $('#sel_runners').change(function(){
       var selected = $(this).find('option:selected');
       $('#name').val(selected.data('name'));
       $('#display_name').val(selected.data('display_name'))
       $('#twitch').val(selected.data('twitch'));
       $('#twitter').val(selected.data('twitter'));
       $('#youtube').val(selected.data('youtube'));
    });
});