async function send() {
    const input = document.getElementById("msg");
    const sendBtn = document.querySelector(".input-area button");
    const message = input.value.trim();
    
    if (!message) return;

    // Add user message immediately
    addMessage(message, "user");
    input.value = "";
    
    // Disable input while bot is thinking
    input.disabled = true;
    sendBtn.disabled = true;

    // Show typing indicator
    const loadingDiv = showTypingIndicator();

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await res.json();
        
        loadingDiv.remove();
        // Add bot response with typing animation
        addMessage(data.reply, "bot", true); 

    } catch (error) {
        if (loadingDiv) loadingDiv.remove();
        // Neutral error message (English, as network error doesn't know user's language)
        addMessage("Sorry, a connection error occurred. Please try again.", "bot");
    } finally {
        input.disabled = false;
        sendBtn.disabled = false;
        input.focus();
    }
}

function addMessage(text, cls, animate = false) {
    const box = document.getElementById("chatbox");
    const div = document.createElement("div");
    div.className = cls;
    box.appendChild(div);

    if (animate && cls === "bot") {
        let i = 0;
        div.textContent = ""; 
        const interval = setInterval(() => {
            div.textContent += text.charAt(i);
            i++;
            box.scrollTop = box.scrollHeight;
            if (i >= text.length) {
                clearInterval(interval);
            }
        }, 20); // typing speed
    } else {
        div.textContent = text;
    }

    box.scrollTop = box.scrollHeight;
}

function showTypingIndicator() {
    const box = document.getElementById("chatbox");
    const div = document.createElement("div");
    div.className = "bot typing-indicator";
    div.innerHTML = "<span></span><span></span><span></span>";
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
    return div;
}

// Support Enter key
document.getElementById("msg").addEventListener("keypress", (e) => {
    if (e.key === "Enter") send();
});