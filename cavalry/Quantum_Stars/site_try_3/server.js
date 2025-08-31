const WebSocket = require('ws');

const wss = new WebSocket.Server({ server: app.listen(3000) });

const matches = {};

wss.on('connection', ws => {
    ws.on('message', message => {
        const { type, data } = JSON.parse(message);

        switch (type) {
            case 'join_match':
                const matchId = data.matchId;
                if (!matches[matchId]) {
                    matches[matchId] = [];
                }
                matches[matchId].push(ws);
                if (matches[matchId].length === 2) {
                    startMatch(matchId);
                }
                break;
        }
    });
});

function startMatch(matchId) {
    const players = matches[matchId];
    if (players.length === 2) {
        const task = generateTask();
        players.forEach(ws => {
            ws.send(JSON.stringify({ type: 'task', data: task }));
        });
    }
}

function generateTask() {
    const num1 = Math.floor(Math.random() * 100);
    const num2 = Math.floor(Math.random() * 100);
    const operation = ['+', '-', '*', '/'][Math.floor(Math.random() * 4)];
    const question = `${num1} ${operation} ${num2}`;
    let answer;
    switch (operation) {
        case '+':
            answer = num1 + num2;
            break;
        case '-':
            answer = num1 - num2;
            break;
        case '*':
            answer = num1 * num2;
            break;
        case '/':
            answer = num1 / num2;
            break;
    }
    return { question, answer };
}
