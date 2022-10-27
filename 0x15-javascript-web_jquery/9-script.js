const $ = window.$;
$.ajax({
  type: '',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  dataType: "jsonp",
  success: (response) => {
    console.log("Not working")
    $('DIV#hello').text(response.hello);
  },
  error: () => {
    console.log('Error loading orders');
  }
});
