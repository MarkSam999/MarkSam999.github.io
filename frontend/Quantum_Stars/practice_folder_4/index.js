document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');
    const progressData = document.getElementById('progress-data');
    const saveProgressButton = document.getElementById('save-progress');

    // Загрузка прогресса пользователя, если доступен
    const loadProgress = () => {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        if (user) {
            progressData.textContent = `Имя пользователя: ${user.username}, Электронная почта: ${user.email}, Прогресс: ${user.progress || 'Прогресса пока нет.'}`;
        }
    };

    // Обработка регистрации пользователя
    registerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('register-username').value;
        const email = document.getElementById('register-email').value;
        const user = { username, email, progress: '' };
        localStorage.setItem(username, JSON.stringify(user));
        alert('Регистрация успешна! Теперь войдите в систему.');
    });

    // Обработка входа пользователя
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('login-username').value;
        const user = JSON.parse(localStorage.getItem(username));
        if (user) {
            localStorage.setItem('currentUser', JSON.stringify(user));
            loadProgress();
        } else {
            alert('Пользователь не найден!');
        }
    });

    // Обработка сохранения прогресса
    saveProgressButton.addEventListener('click', () => {
        let user = JSON.parse(localStorage.getItem('currentUser'));
        if (user) {
            user.progress = 'Пример данных прогресса...'; // Замените реальными данными прогресса
            localStorage.setItem(user.username, JSON.stringify(user));
            localStorage.setItem('currentUser', JSON.stringify(user));
            loadProgress();
        } else {
            alert('Сначала войдите в систему!');
        }
    });

    // Загрузка прогресса при загрузке страницы
    loadProgress();
});
