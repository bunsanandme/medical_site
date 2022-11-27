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

    if ($('#id_undergo_conversion_lap option:selected').text() == "Да") {
        $('#conversion_reason_lap').fadeIn(300);
    } 
    else {
        $('#conversion_reason_lap').fadeOut(300);
    }

    if ($('#id_undergo_conversion_open option:selected').text() == "Да") {
        $('#conversion_reason_open').fadeIn(300);
    } 
    else {
        $('#conversion_reason_open').fadeOut(300);
    }

    if ($('#id_malfunction option:selected').text() == "Другое") {
        $('#malfunction_comment').fadeIn(300);
    } 
    else {
        $('#malfunction_comment').fadeOut(300);
    }

    if ($('#id_local_anesthesy_used option:selected').text() == "Да") {
        $('#type_dose').fadeIn(300);
    } 
    else {
        $('#type_dose').fadeOut(300);
    }

    if ($('#inst_other').is(':checked')) {
        $('#extra_inst').fadeIn(300);
    } 
    else {
        $('#extra_inst').fadeOut(300);
    }

    if ($('#id_brought_ICU option:selected').text() == "Да") {
        $('#extra_dates').fadeIn(300);
    } 
    else {
        $('#extra_dates').fadeOut(300);
    }
      
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
$('#id_undergo_conversion_lap').change(function() {
    if ($('#id_undergo_conversion_lap option:selected').text() == "Да") {  
        $('#conversion_reason_lap').fadeIn(300);
    } 
    else {
        $('#conversion_reason_lap').fadeOut(300);
    }
});

$('#id_undergo_conversion_open').change(function() {
    if ($('#id_undergo_conversion_open option:selected').text() == "Да") {  
        $('#conversion_reason_open').fadeIn(300);
    } 
    else {
        $('#conversion_reason_open').fadeOut(300);
    }
});

$('#id_malfunction').change(function() {
    if ($('#id_malfunction option:selected').text() == "Другое") {
        $('#malfunction_comment').fadeIn(300);
    } 
    else {
        $('#malfunction_comment').fadeOut(300);
    }
});

$('#id_local_anesthesy_used').change(function() {
    if ($('#id_local_anesthesy_used option:selected').text() == "Да") {
        $('#type_dose').fadeIn(300);
    } 
    else {
        $('#type_dose').fadeOut(300);
    }
});

$('#inst_other').click(function() {
    if ($('#inst_other').is(':checked')) {
        $('#extra_inst').fadeIn(300);
    } 
    else {
        $('#extra_inst').fadeOut(300);
    }
});

$('#id_brought_ICU').change(function() {
    if ($('#id_brought_ICU option:selected').text() == "Да") {
        $('#extra_dates').fadeIn(300);
    } 
    else {
        $('#extra_dates').fadeOut(300);
    }
});
});