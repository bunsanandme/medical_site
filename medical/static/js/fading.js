$(document).ready(function() {


    if ($('#smoker option:selected').text() == "Да") {
        $('#packyears').fadeIn(300);
    } 
    else {
        $('#packyears').fadeOut(300);
    }

    if ($('#id_relevant_disease option:selected').text() == "Да") {
        $('#diseasetable').fadeIn(300);
    } 
    else {
        $('#diseasetable').fadeOut(300);
    }
    
    
    if ($('#id_has_abdominal_surgery option:selected').text() == "Да") {
    $('#surgion_description').fadeIn(300);
    } 
    else {
    $('#surgion_description').fadeOut(300);
    }
});

      
$("#smoker").change(function() {
    if ($('#smoker option:selected').text() == "Да") {
        $('#packyears').fadeIn(300);
    } 
    else {
        $('#packyears').fadeOut(300);
    }   
    });

$("#id_relevant_disease").change(function() {
    if ($('#id_relevant_disease option:selected').text() == "Да") {
    $('#diseasetable').fadeIn(300);
    } 
    else {
    $('#diseasetable').fadeOut(300);
    }
});

$('#id_has_abdominal_surgery').change(function() {
    if ($('#id_has_abdominal_surgery option:selected').text() == "Да") {
        $('#surgion_description').fadeIn(300);
    } 
    else {
        $('#surgion_description').fadeOut(300);
    }

});