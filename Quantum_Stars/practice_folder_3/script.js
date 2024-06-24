const form = document.querySelector("form");

function sendEmail() {
    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "marksamoylov2008@gmail.com",
        Password : "7422B263230779EF4FB37811081AEE88339B",
        To : 'marksamoylov2008@gmail.com',
        From : "marksamoylov2008@gmail.com",
        Subject : "This is the subject",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    sendEmail();
});