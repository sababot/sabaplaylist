var playlist_loaded = 0;
var playlist_tracks = 0;
var playlist_length = "";
var playlist_name = "";

function get_variables() {
  $.getJSON('/get_vars', function(data) {
    playlist_loaded = data.playlist_loaded;
    playlist_tracks = data.playlist_tracks;
    playlist_lengths = data.playlist_length;
    playlist_name = data.playlist_name;
  });

  document.getElementById("playlist_tracks").innerHTML = "tracks: " + playlist_tracks;

  if (playlist_loaded == 1)
    document.getElementById("playlist_loaded").innerHTML = "loaded: true";
  else
    document.getElementById("playlist_loaded").innerHTML = "loaded: false";
}

get_variables();

function load_playlist() {
  var playlist_id = document.getElementById("search_input").value;
  $.getJSON('/load_playlist/' + playlist_id, function(data) {
      playlist_loaded = data.playlist_loaded;
      playlist_tracks = data.playlist_tracks;
    });

  get_variables();

  if (playlist_loaded == 1) {
    document.getElementById("search_input").readOnly = true;
  }
}

function export_playlist() {
  var playlist_id = document.getElementById("search_input").value;
  
  get_variables();

  if (playlist_loaded == 1) {
    window.location.href = '/export_playlist/' + playlist_id;
    $.getJSON('/export_playlist/' + playlist_id, function(data) {
      // do nothing
    });
  }
}

function new_playlist() {
  $.getJSON('/new_playlist', function(data) {
      // nothing
    });
}

document.getElementById("search_input").addEventListener("input", e => {
  load_playlist();
})

document.getElementById('search_input').onkeypress = function(e){
    if (!e) e = window.event;
    var keyCode = e.code || e.key;
    if (keyCode == 'Enter'){
      load_playlist();

      return false;
    }
  }