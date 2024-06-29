document.addEventListener('DOMContentLoaded', function() {
    const addFewshotButton = document.getElementById('addFewshotButton');
    const fewshotInputContainer = document.getElementById('fewshotInputContainer');
    let inputCount = 1;

    addFewshotButton.addEventListener('click', function() {
        if (inputCount < 3) {
            inputCount++;
            const newTextInputContainer = document.createElement('div');
            newTextInputContainer.classList.add('large-text-input-container');
            newTextInputContainer.innerHTML = `<textarea type="text" id="fewshotInput${inputCount}" class="textarea-box" placeholder="Optional few-shot input"></textarea>`;
            fewshotInputContainer.insertAdjacentElement('afterend', newTextInputContainer);
            if (inputCount === 3) {
                addFewshotButton.disabled = true;
            }
        } else {
            addFewshotButton.disabled = true;
        }
    });
});
