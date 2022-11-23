jQuery(function($) {
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

        let weight  = $("#height");
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
                '<div class="alert alert-danger" role="alert" id="error">Возникли ошибки при заполнении:<ul>' + 
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
      if ($('#id_relevant_disease option:selected').text() == "Да" && !Boolean($('input[type="checkbox"]').is(':checked'))) {
        var v_rd = true;
        error_string += '<li> Не отмечено хотя бы одной болезни </li>';
    }
    let validate = v_rd;
    if (validate) {
      $("#form_mh").before(
          '<div class="alert alert-danger" role="alert" id="error">Возникли ошибки при заполнении:<ul>' + 
          error_string + 
          '</ul></div>');
    }
    return validate;
    }

});

});