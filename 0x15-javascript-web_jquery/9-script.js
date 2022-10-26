$(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
      if (textStatus === 'success') {
        $('#sf_wind_speed').text(data.query.hello);
      }
    });
  });
