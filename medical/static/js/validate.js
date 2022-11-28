jQuery(function($) {

  function isEmpty(str) {
    return (!str || 0 === str.length);
  }

  $('#form_preproc').on('submit', function(event) {
    if ( validateForm_preproc() ) {
      event.preventDefault();
    }
  
  function validateForm_preproc() {
    $("#error").remove();
    let error_string = "";
    let now = new Date().valueOf();

    let creation_date  = $("#id_creation_date");
    if (Date.parse(creation_date.val()) > now ) {
      var v_creation_date = true;
      error_string += '<li> Дата создания записи не может быть больше сегодняшней </li>';
    }

    let sign_date  = $("#id_sign_date");
    if (Date.parse(sign_date.val()) > now ) {
      var v_sign_date = true;
      error_string += '<li> Дата подписания соглашения не может быть больше сегодняшней </li>';
    }

    let admission_date  = $("#id_admission_date");
    if (Date.parse(admission_date.val()) > now ) {
      var v_admission_date = true;
      error_string += '<li> Дата приема не может быть больше сегодняшней </li>';
    }

    let height  = $("#height");
    if ( Number(height.val()) > 300 || Number(height.val()) < 1) {
      var v_height = true;
      error_string += '<li> Неверное значение поля "Рост" </li>';
    }

    let weight  = $("#weight");
    if ( Number(weight.val()) > 300 || Number(weight.val()) < 1) {
        var v_weight = true;
        error_string += '<li> Неверное значение поля "Вес" </li>';
    }

    if ($('#smoker option:selected').text() == "Да" && $('#packyears').children().last().val() == 0 ) {
        var v_smoker = true;
        error_string += '<li> Стаж курения должен быть больше нуля </li>'
    }

    let validate = v_height || v_weight || v_admission_date || v_sign_date || v_creation_date || v_smoker;
    if (validate) {
        $("#form_preproc").before(
            '<div class="alert alert-danger" role="alert" id="error">' +
            'Возникли ошибки при заполнении:<ul>' + 
            error_string + 
            '</ul></div>');
    }
    return validate;
  }

});



$('#form_mh').on('submit', function(event) {
  if ( validateForm_mh() ) {
    event.preventDefault();
  }

function validateForm_mh() {
  $("#error").remove();
  let error_string = "";

  let checked = [];
  let checks = $("#form_mh").find('input:checkbox:checked');

  checks.each(function() {
	  checked.push($(this).val());
  });

  if($('#id_relevant_disease option:selected').text() == "Да" && checked.length == 0) {
    var v_diseases = true;
    error_string += "<li>Не выбрано ни одной болезни</li>";
  }

  let validate = v_diseases;
  if (validate) {
      $("#form_mh").before(
          '<div class="alert alert-danger" role="alert" id="error">' +
          'Возникли ошибки при заполнении:<ul>' + 
          error_string + 
          '</ul></div>');
  }
  return validate;
}

});



$('#form_sh').on('submit', function(event) {
  if ( validateForm_sh() ) {
    event.preventDefault();
  };

function validateForm_sh() {
  $("#error").remove();

  let error_string = "";
  if($('#id_has_abdominal_surgery option:selected').text() == "Да" && isEmpty($('#form_sh').find("textarea").val())) {
    var v_surgeon = true;
    error_string += "<li>Описание не заполнено</li>";
  };

  let validate = v_surgeon;
  if (validate) {
      $("#form_sh").before(
          '<div class="alert alert-danger" role="alert" id="error">' +
          'Возникли ошибки при заполнении:<ul>' + 
          error_string + 
          '</ul></div>');
  };
  return validate;
};
});


$('#form_gp').on('submit', function(event) {
  if ( validateForm_gp() ) {
    event.preventDefault();
  }

function validateForm_gp() {
  $("#error").remove();
  let error_string = "";

  let checked = [];
  let checks = $("#form_gp").find('input:checkbox:checked');

  checks.each(function() {
	  checked.push($(this).val());
  });

  if($('other_gastro').val() == '' || checked.length == 0) {
    var v_diseases = true;
    error_string += "<li>Не выбрано ни одной процедуры</li>";
  }

  let validate = v_diseases;
  if (validate) {
      $("#form_gp").before(
          '<div class="alert alert-danger" role="alert" id="error">' +
          'Возникли ошибки при заполнении:<ul>' + 
          error_string + 
          '</ul></div>');
  }
  return validate;
}
});


$('#form_up').on('submit', function(event) {
  if ( validateForm_up() ) {
    event.preventDefault();
  }

function validateForm_up() {
  $("#error").remove();
  let error_string = "";

  let checked = [];
  let checks = $("#form_up").find('input:checkbox:checked');

  checks.each(function() {
	  checked.push($(this).val());
  });

  if($('other_uro').val() == '' || checked.length == 0) {
    var v_diseases = true;
    error_string += "<li>Не выбрано ни одной процедуры</li>";
  }

  let validate = v_diseases;
  if (validate) {
      $("#form_up").before(
          '<div class="alert alert-danger" role="alert" id="error">' +
          'Возникли ошибки при заполнении:<ul>' + 
          error_string + 
          '</ul></div>');
  }
  return validate;
}
});

});