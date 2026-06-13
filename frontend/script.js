const startBtn = document.getElementById('start-btn');
const sceneText = document.getElementById('scene-text');
const choicesContainer = document.getElementById('choices-container');
const sceneImage = document.getElementById('scene-image');
const statsBar = {
    sanity: document.getElementById('sanity-val'),
    health: document.getElementById('health-val'),
    level: document.getElementById('level-val')
};

let audioCtx;
let oscillator;
let gainNode;
let isMuted = false;
function initAudio() {
    try {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            oscillator = audioCtx.createOscillator();
            gainNode = audioCtx.createGain();

            oscillator.type = 'sawtooth';
            oscillator.frequency.value = 50;
            gainNode.gain.value = 0.05;

            oscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            oscillator.start();
            const lfo = audioCtx.createOscillator();
            const lfoGain = audioCtx.createGain();
            lfo.frequency.value = 0.1; 
            lfoGain.gain.value = 10;
            lfo.connect(lfoGain);
            lfoGain.connect(oscillator.frequency);
            lfo.start();
        } else if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
    } catch (e) {
        console.warn("Audio initialization failed (likely browser policy):", e);
    }
}

function playHapticFeedback(pattern) {
    if (navigator.vibrate) {
        try {
            navigator.vibrate(pattern);
        } catch (e) { console.log("Haptics not supported"); }
    }
}

async function startGame() {
    console.log("Game starting...");
    initAudio();

    startBtn.innerText = "LOADING NIGHTMARE...";
    startBtn.disabled = true;

    try {
        const response = await fetch('/api/start', { method: 'POST' });
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        console.log("Start data received:", data);
        updateUI(data);
    } catch (error) {
        console.error("Error starting game:", error);
        sceneText.innerText = "Connection to the nightmare failed. Server might be down or unreachable.";
        sceneText.style.color = "red";
        startBtn.innerText = "RETRY CONNECTION";
        startBtn.disabled = false;
    }
}

async function makeChoice(index) {
    playHapticFeedback(50);
    const buttons = choicesContainer.querySelectorAll('button');
    buttons.forEach(b => b.disabled = true);

    try {
        const response = await fetch('/api/choice', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ choice_index: index })
        });
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        console.log("Choice data received:", data);

        if (data.game_over) {
            handleGameOver(data);
        } else {
            updateUI(data);
        }
    } catch (error) {
        console.error("Error making choice:", error);
        sceneText.innerText = "The darkness refuses to answer... (Network Error)";
        // Re-enable buttons if it failed
        buttons.forEach(b => b.disabled = false);
    }
}

function updateUI(data) {
    if (!data) {
        console.error("No data received for updateUI");
        return;
    }
    sceneText.style.opacity = 0;
    setTimeout(() => {
        sceneText.innerText = data.message || "The void is silent.";
        sceneText.style.opacity = 1;
        sceneText.parentElement.classList.add('glitching');
        setTimeout(() => sceneText.parentElement.classList.remove('glitching'), 500);
    }, 200);

    if (data.stats) {
        statsBar.sanity.innerText = data.stats.sanity;
        statsBar.health.innerText = data.stats.health;
        statsBar.level.innerText = data.stats.level;
        if (data.stats.health < 30) {
            document.body.style.boxShadow = "inset 0 0 100px red";
            playHapticFeedback([100, 50, 100, 50, 100]); 
        } else {
            document.body.style.boxShadow = "none";
        }
    }

    if (data.image) {
        sceneImage.style.display = 'block';
        sceneImage.src = data.image;
        sceneImage.onerror = function () {
            this.style.display = 'none';
        };
    }
    choicesContainer.innerHTML = '';
    choicesContainer.className = 'choices';

    if (data.choices && data.choices.length > 0) {
        data.choices.forEach((choice, index) => {
            const btn = document.createElement('button');
            btn.innerText = choice.text;
            btn.onclick = () => makeChoice(index);
            choicesContainer.appendChild(btn);
        });
    } else if (!data.game_over) {
        choicesContainer.innerHTML = '<p class="stat">...waiting...</p>';
    }
}

function handleGameOver(data) {
    sceneText.innerText = data.message;
    sceneText.style.color = "red";
    sceneText.style.fontSize = "1.5rem";
    choicesContainer.innerHTML = '<button onclick="location.reload()">TRY AGAIN IF YOU DARE</button>';
    playHapticFeedback([200, 100, 500]);
    if (audioCtx && oscillator) {
        oscillator.frequency.value = 20;
    }
}

startBtn.addEventListener('click', startGame);

document.getElementById('mute-btn').addEventListener('click', () => {
    if (audioCtx && gainNode) {
        if (isMuted) {
            gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime);
            isMuted = false;
        } else {
            gainNode.gain.setValueAtTime(0, audioCtx.currentTime);
            isMuted = true;
        }
    }
});
