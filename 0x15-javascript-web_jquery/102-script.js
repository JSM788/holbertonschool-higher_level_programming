$('INPUT#btn_translate').click(function () {
  const lang = $('INPUT#language_code').val();
  const url = 'https://stefanbohacek.com/hellosalut/?lang=' + lang;
  $.getJSON(url,
    function (data) {
      $('DIV#hello').html(data.hello);
  });
});     
