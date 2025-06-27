// app.js

// Initialize Firebase
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();
const db = firebase.firestore();

// Listen to auth state changes
auth.onAuthStateChanged(user => {
    if (user) {
        // User is signed in, redirect to menu
        window.location.href = 'menu.html';
    }
});

function signUp() {
    const email = document.getElementById('sign-up-email').value;
    const password = document.getElementById('sign-up-password').value;
    auth.createUserWithEmailAndPassword(email, password)
        .then(userCredential => {
            console.log('User signed up:', userCredential.user);
            window.location.href = 'menu.html'; // Redirect after sign up
        })
        .catch(error => {
            console.error('Error signing up:', error);
        });
}

function signIn() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    auth.signInWithEmailAndPassword(email, password)
        .then(userCredential => {
            console.log('User signed in:', userCredential.user);
            window.location.href = 'menu.html'; // Redirect after sign in
        })
        .catch(error => {
            console.error('Error signing in:', error);
        });
}

// Functions for menu.html
function saveProgress() {
    const user = auth.currentUser;
    if (user) {
        const userData = {
            score: 100, // Example data
            level: 5   // Example data
        };
        db.collection('users').doc(user.uid).set(userData)
            .then(() => {
                console.log('User progress saved');
            })
            .catch(error => {
                console.error('Error saving progress:', error);
            });
    }
}

function loadUserData(userId) {
    db.collection('users').doc(userId).get()
        .then(doc => {
            if (doc.exists) {
                const userData = doc.data();
                console.log('User data:', userData);
                // Use this data to update the UI or game state
            } else {
                console.log('No such document!');
            }
        })
        .catch(error => {
            console.error('Error getting document:', error);
        });
}

function signOut() {
    auth.signOut()
        .then(() => {
            console.log('User signed out');
            window.location.href = 'index.html'; // Redirect after sign out
        })
        .catch(error => {
            console.error('Error signing out:', error);
        });
}

function showSignUpForm() {
    document.getElementById('sign-in-form').style.display = 'none';
    document.getElementById('sign-up-form').style.display = 'block';
}

function showSignInForm() {
    document.getElementById('sign-in-form').style.display = 'block';
    document.getElementById('sign-up-form').style.display = 'none';
}

function createMatch() {
    const user = auth.currentUser;
    if (user) {
        db.collection('matches').add({
            userId: user.uid,
            score: 0,
            timestamp: firebase.firestore.FieldValue.serverTimestamp()
        }).then(docRef => {
            console.log('Match created with ID:', docRef.id);
        }).catch(error => {
            console.error('Error creating match:', error);
        });
    } else {
        console.error('User not authenticated');
    }
}

function joinMatch() {
    const user = auth.currentUser;
    if (user) {
        db.collection('matches').where('opponentId', '==', null).limit(1).get()
            .then(querySnapshot => {
                if (!querySnapshot.empty) {
                    const match = querySnapshot.docs[0];
                    match.ref.update({
                        opponentId: user.uid
                    }).then(() => {
                        console.log('Joined match:', match.id);
                    });
                } else {
                    console.log('No available matches, creating a new one');
                    createMatch();
                }
            }).catch(error => {
                console.error('Error joining match:', error);
            });
    } else {
        console.error('User not authenticated');
    }
}

function updateScore(matchId, userId, points) {
    db.collection('matches').doc(matchId).update({
        [`scores.${userId}`]: firebase.firestore.FieldValue.increment(points)
    }).then(() => {
        console.log('Score updated');
    }).catch(error => {
        console.error('Error updating score:', error);
    });
}

function startGame() {
    const task = generateTask();
    document.getElementById('task-container').innerText = task.question;
    window.currentAnswer = task.answer;
    document.getElementById('menu-container').style.display = 'none';
    document.getElementById('game-container').style.display = 'block';
}

function submitAnswer() {
    const userAnswer = parseInt(document.getElementById('answer').value);
    if (userAnswer === window.currentAnswer) {
        console.log('Correct!');
        // Update score, etc.
    } else {
        console.log('Incorrect.');
    }
}

