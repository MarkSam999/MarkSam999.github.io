// taskGenerator.js

function generateTask() {
    const operations = ['+', '-', '*', '/'];
    const num1 = Math.floor(Math.random() * 100);
    const num2 = Math.floor(Math.random() * 100);
    const operation = operations[Math.floor(Math.random() * operations.length)];

    let question, answer;
    switch (operation) {
        case '+':
            question = `${num1} + ${num2}`;
            answer = num1 + num2;
            break;
        case '-':
            question = `${num1} - ${num2}`;
            answer = num1 - num2;
            break;
        case '*':
            question = `${num1} * ${num2}`;
            answer = num1 * num2;
            break;
        case '/':
            question = `${num1} / ${num2}`;
            answer = num1 / num2;
            break;
    }
    return { question, answer };
}

// Usage example
const task = generateTask();
console.log(`Question: ${task.question}, Answer: ${task.answer}`);
