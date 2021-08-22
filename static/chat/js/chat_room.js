const chatRoomName = JSON.parse(document.getElementById('chat-room-name').textContent);
const parsedUsername = JSON.parse(document.getElementById('username').textContent);
const timeNow = new Date().toLocaleTimeString().slice(0,-3);
const username = parsedUsername ? parsedUsername : 'Anonymous';
const messages = document.getElementById('msger-chatarea');
messages.scrollTop = messages.scrollHeight;
let counter = updateCounter();

function updateCounter(){
    if (document.querySelector('#msger-chatarea').lastElementChild){
        return Number(document.querySelector('#msger-chatarea').lastElementChild.id) + 1;
    } else {
        return 1;
    }
}
function inputMessage(){
    const messageInputDom = document.querySelector('#input');
    if (messageInputDom.value){
    chatSocket.send(JSON.stringify({
        'author': username,
        'message': messageInputDom.value,
        'time': timeNow,
        'room': chatRoomName,
        'count': counter
    }))}else {
        alert('Вы не можете отправить пустое сообщение :(')
    }
    messageInputDom.value = '';
}
function insertHTMLright(data){
    document.querySelector('#msger-chatarea').insertAdjacentHTML('beforeend', `
    <div class="msg right-msg" id = "${String(counter)}">
        <div
        class="msg-img"
        style="background-image: url(https://image.flaticon.com/icons/svg/145/145867.svg)"
        ></div>
        
        <div class="msg-bubble">
            <div class="msg-info">
              <div class="msg-info-name">${data.author + ':'}</div>
              <div class="msg-info-time">${data.time}</div>
            </div>
            <div class="msg-text">${data.message}</div>
        </div>
    </div>
    `);
}
function insertHTMLleft(data){
    document.querySelector('#msger-chatarea').insertAdjacentHTML('beforeend', `
    <div class="msg left-msg" id = "${String(counter)}">
        <div
        class="msg-img left-msg"
        style="background-image: url(https://image.flaticon.com/icons/svg/145/145867.svg)"
        ></div>
        
        <div class="msg-bubble left-msg">
            <div class="msg-info">
              <div class="msg-info-name">${data.author + ':'}</div>
              <div class="msg-info-time">${data.time}</div>
            </div>
            <div class="msg-text">${data.message}</div>
        </div>
    </div>
    `);
}

const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + chatRoomName + '/');

chatSocket.onmessage = function (e){
    const data = JSON.parse(e.data);
    console.log(data);
    if (data.count % 2 === 0){
        insertHTMLright(data)
        counter ++
    } else {
        insertHTMLleft(data)
        counter ++
    }

    messages.scrollTop = messages.scrollHeight;
    };

document.querySelector('#submit').onclick = inputMessage;
document.querySelector('#input').addEventListener('keypress', function (e){
    if (e.key === 'Enter'){
        e.preventDefault()
        inputMessage()
    }
});
