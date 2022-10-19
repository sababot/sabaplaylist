function export_playlist() {
  var playlist_id = document.getElementById("search_input").value.toLowerCase();
  $.getJSON('/export_playlist', function(playlist_id) {
    // do nothing
  });
}