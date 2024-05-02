$(document).ready(function() {
    //change playing mode
    var autoPauseEnabled = true; // default auto pause 
    var currentAudio = null; // now playing audio

    $('#site-title').click(function(){
        //back to top
        $('html, body').animate({scrollTop : 0},0);
        return false;
    });

    $('.lang-switch').click(function() {
        var lang = $(this).data('lang');
        switchLanguage(lang);
    });
    
    $(".play-audio").click(function(){
        // get audio name
        var audioFileName = $(this).data('audio');
    
        // get audio url
        var encodedFileName = encodeURIComponent(audioFileName);
        var audioFile = '/static/audios/' + encodedFileName;
        // if autoPause on and now playing audio
        if (autoPauseEnabled && currentAudio !== null) {
            currentAudio.pause();
        }
    
        // create new audio element
        var audio = new Audio(audioFile);
        audio.play();
    
        // set audio
        currentAudio = audio;
    });

    $("#voice_pause").click(function(){
        //change statement
        autoPauseEnabled = !autoPauseEnabled;
    });
});

function switchLanguage(lang) {
    // switch site's language
    var postData = { "lang": lang };
    $.when(
        $.ajax({
            url: '/data_request',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify(postData),
            contentType: 'application/json'
        })
    ).done(function(textsData) {
        updateTexts(textsData);
        document.title = textsData.title; // update title
    }).fail(function(error) {
        console.error('Error fetching language files:', error);
    });

    $('html').attr('lang', lang); //change html attr
}

function updateTexts(texts) {
    //change all text via tags
    $.each(texts, function(categoryTag, data) {
        if (data !=null){
            $('#' + categoryTag).text(data);
        }
    });
}
