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
        var volume_setting = document.querySelector("#volumeRange");

        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        var source = audioCtx.createMediaElementSource(audio);
        var gainNode = audioCtx.createGain();
        function f(x) {
            return x*0.01;
        }
        gainNode.gain.value = f(volume_setting.value) // increase the volume above 100%
        source.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        
        
        audio.play();
    
        // set audio
        currentAudio = audio;
    });

    $("#voice-pause").click(function(){
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

// Define a function to handle input range elements with class 'slider-progress'
function handleSliderProgress() {
    // Get all input range elements with class 'slider-progress'
    const sliders = document.querySelectorAll('input[type="range"].slider-progress');

    // Loop through each input range element
    sliders.forEach(slider => {
        // Set initial CSS custom properties based on the input attributes
        slider.style.setProperty('--value', slider.value);
        slider.style.setProperty('--min', slider.min === '' ? '0' : slider.min);
        slider.style.setProperty('--max', slider.max === '' ? '100' : slider.max);

        // Add event listener for 'input' event to update CSS custom property '--value'
        slider.addEventListener('input', () => {
            slider.style.setProperty('--value', slider.value);
        });
    });
}

// Call the function to handle slider progress elements when the DOM content is loaded
document.addEventListener('DOMContentLoaded', handleSliderProgress);
