// 翻訳ボタンと入力フィールドの要素を取得
const inputText = document.getElementById('inputText');
const outputText = document.getElementById('outputText');
const sourceLanguage = document.getElementById('sourceLanguage');
const targetLanguage = document.getElementById('targetLanguage');
const translateButton = document.getElementById('translateButton');

// 翻訳ボタンのクリックイベント
translateButton.addEventListener('click', translateText);

// 翻訳関数
async function translateText() {
    const text = inputText.value.trim();
    if (!text) {
        outputText.value = '';
        alert('Please enter text to translate.');
        return;
    }

    try {
        // 翻訳リクエストを送信
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                source_language: sourceLanguage.value,
                target_language: targetLanguage.value
            })
        });

        // レスポンスをJSON形式で取得
        const data = await response.json();
        if (data.error) {
            outputText.value = `Error: ${data.error}`;
        } else {
            outputText.value = data.translated_text;
        }
    } catch (error) {
        outputText.value = `Error: ${error.message}`;
    }
}