$(document).ready(function() {
    //change playing mode
    var autoPauseEnabled; // default auto pause 
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
        var cut_setting = document.getElementById("flexCheckChecked");
        if (cut_setting.checked){
            autoPauseEnabled = true;
            $('.play-audio .progress').remove();
        }else{
            autoPauseEnabled = false;
            $(this).find('.progress').remove();
        }
        if (autoPauseEnabled && currentAudio !== null) {
            currentAudio.pause();
        }
    
        // create new audio element
        var audio = new Audio(audioFile);
        var volume_setting = document.querySelector("#volumeRange");

        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        var source = audioCtx.createMediaElementSource(audio);
        var gainNode = audioCtx.createGain();

        var inputNode = audioCtx.createGain();
        var reverbNode = audioCtx.createConvolver();
        var outputNode = audioCtx.createGain();
        var wet = audioCtx.createGain();
        var dry = audioCtx.createGain();

        function f(x) {
            return x*0.01;
        }
        gainNode.gain.value = f(volume_setting.value) // increase the volume above 100%

        var echo_setting = document.querySelector("#echoCheckChecked");
        if (echo_setting.value == 0){
            source.connect(gainNode);
            gainNode.connect(audioCtx.destination);
        }else{
            var sampleRate = audioCtx.sampleRate;
            var length = sampleRate * (echo_setting.value / 33); // 2 seconds
            var impulse = audioCtx.createBuffer(2, length, sampleRate);
            var impulseL = impulse.getChannelData(0);
            var impulseR = impulse.getChannelData(1);

            for (var i = 0; i < length; i++) {
                impulseL[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, 1);
                impulseR[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / length, 1);
            }
            wet.gain.value = 0.5;
            dry.gain.value = 0.5;
            reverbNode.buffer = impulse;
            
            source.connect(gainNode);
            gainNode.connect(inputNode);

            inputNode.connect(reverbNode);
            reverbNode.connect(wet);
            inputNode.connect(dry);
            dry.connect(outputNode);
            wet.connect(outputNode);
            outputNode.connect(audioCtx.destination);
        }

        // Check if progress bar already exists

        const progressContainer = $('<div>').addClass('progress');
        const progressBar = $('<div>').addClass('progress-bar').css('width', '0%');
        progressContainer.append(progressBar);
        $(this).append(progressContainer);
        // Start the progress bar animation
        const interval = 100; // Update interval in milliseconds
        
        progressInterval = setInterval(() => {
            const progress = (audio.currentTime / audio.duration) * 100;
            progressBar.css('width', progress + '%');
        }, interval);

        audio.play();
    
        // set audio
        currentAudio = audio;
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
