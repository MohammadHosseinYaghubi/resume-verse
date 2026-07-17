document.addEventListener('DOMContentLoaded', function() {
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotWindow = document.getElementById('chatbot-window');
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSendBtn = document.getElementById('chat-send-btn');

    if (chatbotToggle && chatbotWindow && chatMessages && chatInput && chatSendBtn) {
        chatbotToggle.addEventListener('click', function() {
            chatbotWindow.classList.toggle('d-none');
        });

        chatSendBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        function sendMessage() {
            const userMessage = chatInput.value.trim();
            if (userMessage === '') return;

            appendMessage('user', userMessage);
            chatInput.value = '';

            // Simulate bot response
            setTimeout(() => {
                const botResponse = getBotResponse(userMessage);
                appendMessage('bot', botResponse);
            }, 500);
        }

        function appendMessage(sender, text) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('chat-message', sender);
            messageElement.textContent = text;
            chatMessages.appendChild(messageElement);
            chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
        }

        function getBotResponse(message) {
            message = message.toLowerCase();
            if (message.includes('hello') || message.includes('hi')) {
                return 'Hello! How can I help you with Mohammad Hossein Yaghubi\'s resume?';
            } else if (message.includes('experience')) {
                return 'Mohammad Hossein has experience as a darsman.';
            } else if (message.includes('education')) {
                return 'Mohammad Hossein has a Bachelor of Power Engineering from Sajjad University of Technology.';
            } else if (message.includes('skills')) {
                return 'Mohammad Hossein\'s skills include python, django, mysql, mongodb, and django rest framework.';
            } else if (message.includes('projects')) {
                return 'You can find a list of projects in the "My Projects" section on this page.';
            } else if (message.includes('contact')) {
                return 'You can find contact information at the top of the resume.';
            } else {
                return 'I am a simple chatbot. Please ask about experience, education, skills, projects, or contact information.';
            }
        }

    }
});
