function export_playlist() {
  var playlist_id = document.getElementById("search_input").value;
  window.location.href = '/export_playlist/' + playlist_id;
  //$.getJSON('/export_playlist/' + playlist_id, function(data) {
    // do nothing
  //});
}